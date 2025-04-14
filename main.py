from aes.encryption import encryption
from aes.decryption import decryption
from utils.file_io import read_file, write_file
from utils.data_utils import format_key, split_blocks, join_blocks, bytes_to_hex, hex_to_bytes

def main():
    text_input = read_file("data/input.txt")
    key_input = read_file("data/key.txt")

    key_hex = format_key(key_input)
    plaintext_blocks = split_blocks(text_input)

    # Mã hóa
    ciphertext_blocks = [encryption(bytes_to_hex(b), key_hex) for b in plaintext_blocks]
    merged_ciphertext_hex = ''.join(ciphertext_blocks)

    # Giải mã
    decrypted_blocks = [decryption(ct, key_hex) for ct in ciphertext_blocks]
    decrypted_bytes = join_blocks([hex_to_bytes(d) for d in decrypted_blocks])
    decrypted_text = decrypted_bytes.decode("utf-8", errors="ignore")
    decrypted_text_hex = bytes_to_hex(decrypted_bytes)

    # Ghi kết quả ra file
    output_content = (
        f"Plaintext (hex):\n{bytes_to_hex(b''.join(plaintext_blocks))}\n\n"
        f"Key (hex):\n{key_hex}\n\n"
        f"Ciphertext (hex):\n{merged_ciphertext_hex}\n\n"
        f"Decrypted text (hex):\n{decrypted_text_hex}\n\n"
        f"Decrypted text:\n{decrypted_text}\n"
    )
    write_file("data/file.txt", output_content)

if __name__ == "__main__":
    main()