import subprocess

def read_tool_list(file_path):
    with open(file_path, "r") as file:
        tools = [line.strip() for line in file if line.strip()]
    return tools

def install_kali_tools(tool_list):
    for tool in tool_list:
        print(f"Tentando instalar {tool}...")
        try:
            subprocess.run(["sudo", "apt", "install", "-y", tool], check=True)
            print(f"{tool} instalado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar {tool}: {e}")
            print(f"{tool} não pôde ser instalado. Continuando com a próxima ferramenta.")

if __name__ == "__main__":
    tool_file = "kali_tools.txt"
    tools_to_install = read_tool_list(tool_file)
    install_kali_tools(tools_to_install)
