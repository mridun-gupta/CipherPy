import os

# Define the cipher and decipher sheets
CipherSheet = {
    "A": ".1", "B": ".2", "C": ".3", "D": ".4",
    "E": ".01", "F": ".02", "G": ".03", "H": ".04",
    "I": ".001", "J": ".002", "K": ".003", "L": ".004",
    "M": ".0001", "N": ".0002", "O": ".0003", "P": ".0004",
    "Q": ".00001", "R": ".00002", "S": ".00003", "T": ".00004",
    "U": ".000001", "V": ".000002", "W": ".000003", "X": ".000004",
    "Y": ".0000001", "Z": ".0000002", " ": "#"
}

DecipherSheet = {v: k for k, v in CipherSheet.items()}

# Cipher function
def Cipher(text):
    return "".join(CipherSheet.get(char.upper(), "") for char in text)

# Decipher function
def Decipher(text):
    result = []
    i = 0
    while i < len(text):
        for length in range(9, 0, -1):
            part = text[i:i+length]
            if part in DecipherSheet:
                result.append(DecipherSheet[part])
                i += length
                break
        else:
            i += 1
    return "".join(result)

# Main function
def main():
    mode = input("Do you want to cipher or decipher the text? (Enter 'cipher' or 'decipher'):\n> ").strip().lower()
    if mode not in ["cipher", "decipher"]:
        print("Invalid option. Exiting.")
        return

    source = input("Is the text pasted in the terminal or from a file? (Enter 'terminal' or 'external file'):\n> ").strip().lower()
    if source == "external file":
        file_path = input("Paste the file path:\n> ").strip()
        try:
            with open(file_path, "r") as file:
                text = file.read()
        except FileNotFoundError:
            print("File not found. Exiting.")
            return
    elif source == "terminal":
        text = input("Paste the text:\n> ").strip()
    else:
        print("Invalid option. Exiting.")
        return

    if mode == "cipher":
        result = Cipher(text)
    else:
        result = Decipher(text)

    print("Result:")
    print(result)

    save = input("Do you want to save the result to a file? (Enter 'yes' or 'no'):\n> ").strip().lower()

    if save == "yes":
        file_path = input("Enter the output file path:\n> ").strip()
        with open(file_path, "w") as file:
            file.write(result)
        print(f"Result saved to {file_path}.")
    else:
        print("Operation completed without saving to a file.")

if __name__ == "__main__":
    main()