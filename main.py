import requests
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table

init(autoreset=True)
console = Console()

def info(url):
    try:
        print(Fore.WHITE + Style.BRIGHT + "\nconnecting to the website\n")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html_content = response.text
        num_lines = len(html_content.splitlines())
        file_size_kb = len(html_content.encode("utf-8")) / 1024
        status_code = response.status_code

        return {
            "stat": status_code,
            "lines": num_lines,
            "kb": round(file_size_kb, 2),
            "html_content": html_content
        }
    except requests.exceptions.RequestException as e:
        print(Fore.WHITE + f"\n👉 {e}")
        return None

def dis(info, url):
    table = Table(title=f"website information", title_style="green bold")
    table.add_column("attribute", style="blue bold")
    table.add_column("value", style="red bold")
    table.add_row("website status", str(info["stat"]))
    table.add_row("website lines", str(info["lines"]))
    table.add_row("website size", f"{info['kb']} KB")
    console.print(table)

def save(html_content, file_name="enew.html"):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(Fore.GREEN + f"\nhtml src saved in {file_name}")
    except Exception as e:
        print(Fore.WHITE + f"\n👉 {e}")

if __name__ == "__main__":
    while True:
        url = input(Fore.BLUE + Style.BRIGHT + "\n enter the website url: ").strip()
        if not url.startswith(("http://", "https://")):
            print(Fore.WHITE + "dumb ass.")
            continue

        info = info(url)

        if info:
            dis(info, url)
            save(info["html_content"])
        else:
            print(Fore.WHITE + "failed womp womp")

        cont = input(Fore.WHITE + "\ncheck anth website? (d/n): ").strip().lower()
        if cont != 'd':
            print(Fore.WHITE + "\nbye bye")
            break
