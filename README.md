# 📂 async-views

Repositório dedicado ao exercício do Módulo 12 "Concorrência em Django" do curso "Desenvolvedor Back-end Python" da EBAC. Tratando requisições assíncronas simples com Django, Uvicorn, HTTPX e Asyncio.

<br>

### 📑 Tecnologias usadas:
<table>
  <tr>
    <td>Python</td>
    <td>Django</td>
    <td>HTTPX</td>
    <td>Uvicorn</td>
  </tr>
  <tr>
    <td>3.*</td>
    <td>4.0.6</td>
    <td>0.23</td>
    <td>0.18</td>
  </tr>
</table>

<br>

### Caso queira executar este código e aprender um pouco sobre o funcionamento de processos assíncronos e sincronos

<br>

1) Clone o repositório e entre nele:
```
$ git clone https://github.com/RakelMacedo/async-views.git

$ cd async-views/
```

##

2) No terminal, vamos criar e ativar nosso ambiente virtual:
```bash
$ python3 -m venv venv

$ source venv/bin/activate
```

##

3) Em seguida, vamos baixar as bibliotecas que iremos utilizar:
```bash
$ pip install -r requirements.txt
```

##

4) Vamos rodar nosso Web Server Uvicorn e acessa-lo:
```bash
$ uvicorn --reload asyncviews.asgi:application
```

<br>

Você deverá obter uma saída semelhante a essa:
```bash
INFO:     Will watch for changes in these directories: ['/home/rakel/async-views']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [321558] using StatReload
INFO:     Started server process [321560]
INFO:     Waiting for application startup.
INFO:     ASGI 'lifespan' protocol appears unsupported.
INFO:     Application startup complete.

```

<br>

Acesse pelo o seu navegador http://127.0.0.1:8000/sync *ou* http://127.0.0.1:8000/async, para ver o processo **sincrono** ou **assíncrono** respectivamente. Fique atento ao comportamento Web e do terminal.

<br>

Para o seu melhor aprendizado, aconselho ir em https://docs.python.org/pt-br/3/library/asyncio.html para ler a documentação oficial da biblioteca **asyncio** do Python e modificar o arquivo **views.py** criando novas funções assíncronas. 

<br>

**Saia da zona de conforto, tente, teste, explore, pratique e aprenda.** 😉🤓
