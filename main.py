import struct
import threading

class HashX:
    def __init__(self, seed=0xABCDEF):
        """Initialize hash state with a seed."""
        self.seed = seed
        self.state = [seed, seed ^ 0x12345678, seed ^ 0x87654321, seed ^ 0xFEDCBA98]

    def _mix(self, v):
        """Improved mixing function for better diffusion and security."""
        v ^= v >> 13
        v *= 0x85EBCA6B
        v ^= v >> 16
        v *= 0xC2B2AE35
        v ^= v >> 16
        return v & 0xFFFFFFFFFFFFFFFF  # 64-bit mask

    def _rotate_left(self, x, r):
        """Bitwise left rotation for fast scrambling."""
        return ((x << r) | (x >> (64 - r))) & 0xFFFFFFFFFFFFFFFF

    def _process_chunk(self, chunk, index):
        """Multi-threaded processing of input chunks."""
        v = struct.unpack('<Q', chunk)[0]  # Convert to 64-bit integer
        v = self._mix(v)
        self.state[index % 4] ^= v
        self.state[index % 4] = self._rotate_left(self.state[index % 4], (index * 7) % 64)

    def update(self, data):
        """Process input data in 64-byte chunks with multi-threading."""
        if isinstance(data, str):
            data = data.encode('utf-8')  # Convert string to bytes

        length = len(data)
        padded_data = data + b'\x00' * (64 - (length % 64))  # Padding
        blocks = [padded_data[i:i+8] for i in range(0, len(padded_data), 8)]

        threads = []
        for i, block in enumerate(blocks):
            thread = threading.Thread(target=self._process_chunk, args=(block, i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

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
