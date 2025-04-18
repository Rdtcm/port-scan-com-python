# 🔍 Port Scanner em Python

Um scanner de portas simples feito em Python, ideal para testar a conectividade de portas em um host ou IP. Rápido, prático e sem dependências externas.

---

## ⚙️ Funcionalidades

- Scanner TCP com `socket`
- Permite usar uma lista de portas padrão ou personalizada
- Validação de IP com regex
- Interface em modo texto simples
- Sem necessidade de bibliotecas externas

---

## 📦 Como instalar e usar

### ✅ Pré-requisitos

- Python 3 instalado no sistema
- Permissão para mover arquivos para `/tmp` (usado opcionalmente)

---

### 📁 1. Clonando o repositório

Se este projeto estiver no GitHub, você pode clonar diretamente:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

chmod +x scanner.py

sudo mv scanner.py /tmp/

export PATH=$PATH:/tmp

echo 'export PATH=$PATH:/tmp' >> ~/.bashrc
source ~/.bashrc
```

---

### 🚀 2. Executando o scanner

Após mover o script para o `/tmp` e atualizar o `PATH`, você pode rodar o scanner de qualquer lugar no terminal:

```bash
scanner.py
```

Ou, se preferir rodar diretamente no diretório do projeto:

```bash
python3 scanner.py
```

---

## 🧪 Exemplo de uso

```bash
         />_________________________________ 
[########[]_________________________________>
         \>                                   

                      __                                  ___________           .__
______   ____________/  |_    ______ ____ _____    ____   \__    ___/___   ____ |  |
\____ \ /  _ \_  __ \   __\  /  ___// ___\__  \  /    \    |    | /  _ \ /  _ \|  | 
|  |_> >  <_> )  | \/|  |    \___ \  \___ / __ \|   |  \   |    |(  <_> |  <_> )  |__
|   __/ \____/|__|   |__|   /____  >\___  >____  /___|  /   |____| \____/ \____/|____/
|__|                             \/     \/     \/     \/                              

By Ryan


Write the HOST/IP: 127.0.0.1
Você quer utilizar as portas padrões?[S/N] s

[+] Starting port scanning...

[+] Port 21 is closed!
[+] Port 22 is closed!
[+] Port 23 is closed!
[+] Port 25 is closed!
[+] Port 53 is closed!
[+] Port 80 is closed!
[+] Port 111 is closed!
[+] Port 135 is closed!
[+] Port 139 is closed!
[+] Port 445 is closed!
[+] Port 3306 is closed!
[+] Port 8080 is closed!
[+] Port 9090 is closed!
[+] Port 443 is closed!

[+] Port scanning is finished

```

---

## 🧰 Estrutura do projeto

```
scanner.py         # Script principal
README.md          # Este arquivo
```

---

## 🛡️ Aviso legal

Este projeto é apenas para fins educacionais e de teste em ambientes autorizados. **Não utilize este scanner para invadir ou escanear sistemas sem permissão.** Não me responsabilizo por usos indevidos deste script.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com sugestões, melhorias ou correções.






