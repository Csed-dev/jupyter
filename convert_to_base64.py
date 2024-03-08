import base64
import sys

def image_to_base64(image_path):
    """Konvertiert ein Bild in einen Base64-String."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def save_markdown(markdown, output_file):
    """Speichert den Markdown-Code in einer Datei."""
    with open(output_file, "w") as file:
        file.write(markdown)

def generate_markdown(image_path, base64_string):
    """Erstellt den Markdown-Code für das eingebettete Bild."""
    return f"![Bildbeschreibung](data:image/png;base64,{base64_string})"

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_image> <output_file>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    output_file = sys.argv[2]

    base64_string = image_to_base64(image_path)
    markdown = generate_markdown(image_path, base64_string)
    save_markdown(markdown, output_file)
    
    print(f"Markdown-Code wurde in {output_file} gespeichert.")

if __name__ == "__main__":
    main()
