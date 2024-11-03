# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="https://github.com/lfusca/templateFiap/raw/main/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%"></a>
</p>

<br>

# Sistema de Irrigação Automatizado

# Grupo 35

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/edu-ramos/">Eduardo Ramos</a>

## 👩‍🏫 Professores:

### Tutor(a)

- Lucas

### Coordenador(a)

- André

## 📜 Descrição

Este projeto faz parte da Fase 3 do sistema de gestão agrícola desenvolvido para a empresa **FarmTech Solutions**. O objetivo é criar um sistema de irrigação inteligente que conecta sensores físicos a uma plataforma digital, otimizando a irrigação agrícola.

O sistema utiliza os seguintes componentes:

- **Sensor de Umidade (DHT22)**: Monitora a umidade do solo em tempo real.
- **Sensores de Nutrientes Fósforo (P) e Potássio (K)**: Representados por dois botões, indicando presença ("true") ou ausência ("false") dos nutrientes.
- **Sensor de pH (LDR)**: Um sensor de intensidade de luz que simula os valores de pH do solo.

A bomba d'água é controlada automaticamente com base nas leituras dos sensores, ligando ou desligando conforme as necessidades da lavoura.

**A bomba é ligada quando qualquer uma das seguintes condições é atendida:**

- **Umidade do solo inferior a 30%**: Indica que o solo está seco e necessita de irrigação.
- **Nível de Potássio (K) baixo**: Representado pelo botão de Potássio pressionado (estado "LOW"), indicando deficiência do nutriente.
- **Nível de Fósforo (P) baixo**: Representado pelo botão de Fósforo pressionado (estado "LOW"), indicando deficiência do nutriente.
- **Valor de pH inferior a 6.0**: Determinado pelo sensor LDR, um pH baixo pode afetar a disponibilidade de nutrientes no solo.

Quando nenhuma dessas condições é verdadeira, a bomba é desligada, mantendo o solo em condições ideais.

## 📁 Estrutura de Pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- **src**: Pasta principal com o código-fonte do projeto. Subdividida em:

- **esp32**: Código para o microcontrolador ESP32, responsável pela leitura dos sensores e controle da bomba d'água.

- **python**: Scripts em Python para interagir com o banco de dados, realizando operações CRUD.

- **sql**: Scripts SQL para criação e manutenção do banco de dados, incluindo a tabela `sensor_data`.

- **README.md**: Arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).


## 🔧 Como Executar o Projeto

Siga os passos abaixo para executar o projeto em seu ambiente:

### Pré-requisitos

- **Simulador online Wokwi**
- **Python 3** instalado.
- Bibliotecas Python:
  - `oracledb` (ou a biblioteca correspondente ao seu banco de dados).
- **Banco de Dados SQL**: Pode ser local ou em nuvem.

### Passo a Passo

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/eduduardo/projeto-cap-01-fase-03.git
   ```

2. Acesse a pasta do projeto:

3. Execute o projeto no Wokwi:

- Acesse o link do projeto no Wokwi: https://wokwi.com/projects/413357886293433345
- Clique em `Start Simulation` para iniciar a simulação.
- Observe o funcionamento dos sensores e da bomba d'água.

4. Configurar o Banco de Dados:

- Certifique-se de que o banco de dados SQL está instalado e em execução.
- Utilize o script SQL em `src/sql/banco-de-dados.sql` para criar a tabela sensor_data.
- Configure as credenciais de acesso ao banco de dados no script Python (src/python/projeto.py).

5. Instalar dependências Python:
5.1 Instale as bibliotecas necessárias com o pip:
```
pip install oracledb
```

5.2. Executar o Script Python:

- Na pasta src/python, execute o script:
```
python projeto.py
```

Utilize o menu interativo para realizar operações CRUD no banco de dados.
## 🗃 Histórico de lançamentos

* 0.1.0 *  - 03/11/2024

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

