def format_key(key_str):
    key_bytes = key_str.encode("utf-8")
    key_bytes = key_bytes[:16].ljust(16, b'\x00')
    return key_bytes.hex()

def split_blocks(text_str, block_size=16):
    text_bytes = text_str.encode("utf-8")
    if len(text_bytes) % block_size != 0:
        padding_len = block_size - (len(text_bytes) % block_size)
        text_bytes += b'\x00' * padding_len
    blocks = [text_bytes[i:i+block_size] for i in range(0, len(text_bytes), block_size)]
    return blocks

def join_blocks(blocks):
    byte_data = b''.join(blocks)
    return byte_data.rstrip(b'\x00')

def bytes_to_hex(byte_data):
    return byte_data.hex()

def hex_to_bytes(hex_str):
    return bytes.fromhex(hex_str)