import struct

class HashX:
    def __init__(self, seed=0xABCDEF):
        """Initialize the hash state with a seed."""
        self.seed = seed
        self.state = [seed, seed ^ 0x12345678, seed ^ 0x87654321, seed ^ 0xFEDCBA98]

    def _mix(self, v):
        """Mixing function to ensure diffusion."""
        v ^= v >> 13
        v *= 0x85EBCA6B
        v ^= v >> 16
        return v & 0xFFFFFFFFFFFFFFFF  # 64-bit mask

    def _rotate_left(self, x, r):
        """Bitwise rotation (left)."""
        return ((x << r) | (x >> (64 - r))) & 0xFFFFFFFFFFFFFFFF

    def update(self, data):
        """Process input data in 64-byte chunks."""
        if isinstance(data, str):
            data = data.encode('utf-8')  # Convert string to bytes
        
        length = len(data)
        padded_data = data + b'\x00' * (64 - (length % 64))  # Padding
        blocks = [padded_data[i:i+8] for i in range(0, len(padded_data), 8)]

        for i, block in enumerate(blocks):
            v = struct.unpack('<Q', block)[0]  # Convert to 64-bit integer
            v = self._mix(v)
            self.state[i % 4] ^= v
            self.state[i % 4] = self._rotate_left(self.state[i % 4], (i * 7) % 64)

    def digest(self):
        """Generate final 256-bit hash."""
        final_hash = b''
        for i in range(4):
            self.state[i] = self._mix(self.state[i] ^ (self.seed + i))
            final_hash += struct.pack('<Q', self.state[i])  # Convert back to bytes
        return final_hash.hex()

    def hash(self, data):
        """Convenience function to compute hash in one call."""
        self.update(data)
        return self.digest()

# Example usage:
hasher = HashX()
print(hasher.hash("Hello, World!"))
