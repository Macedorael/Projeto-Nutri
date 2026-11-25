# 🗂️ Minha Vida em Ordem

App para organizar tudo num lugar só, separado em **3 espaços**:

- 👩🏻‍⚕️ **Consultório**: pacientes, consultas, retornos
- **Mac3dos** (com o símbolo da marca): clientes, propostas, reuniões
- 🤍 **Pessoal**: com etiquetas 📚 Estudos, 💪 Academia, 📱 Redes e 🏠 Casa & vida

No topo de toda tela há 4 botões grandes: **🌎 Tudo · Consultório · Mac3dos · Pessoal**.
O número em cada botão mostra quantas tarefas faltam hoje, e o app muda de cor conforme o espaço.
Em **Tudo** você vê a visão geral do dia, com um bloco para cada espaço.
Funciona no celular e no computador, instala como aplicativo e funciona até sem internet.

## O que ele faz

| Tela | Para quê |
|---|---|
| ☀️ **Hoje** | Só o que importa hoje: progresso do dia, **Foco do dia (máx. 3 prioridades)**, tarefas atrasadas (com botão "passar para hoje"), rotina e o que ficou sem data. |
| ✅ **Tarefas** | Todas as tarefas do espaço escolhido. No Pessoal, filtre por Estudos, Academia, Redes ou Casa. |
| 📅 **Agenda** | Próximas 2 semanas e posts programados. Exporta tudo para a agenda do celular. Tem o botão **🗓️ Planejar a semana**. |
| 🔁 **Rotina** | Hábitos diários (água, treino, estudar, story…) com sequência de dias 🔥. |
| 🎬 **Conteúdo** | Quadro das redes: Ideia → Roteiro → Gravado → Editado → Postado. |
| 🎯 **Foco** | Pomodoro (25 min de foco, 5 de pausa) com **uma tarefa só** na tela. |

### Anotar rápido, do seu jeito
Escreva no campo do topo como se fosse um bilhete. O app entende:

- `consulta Ana amanhã 14h` → Consultório, amanhã, lembrete às 14h
- `gravar reels sexta 18h #redes` → Pessoal › Redes, sexta, 18h
- `proposta cliente sexta 10h` → Mac3dos
- `treino todo dia 7h` → Pessoal › Academia, repete todo dia
- `reunião mac3dos segunda às 10`
- `estudar bioquímica 12/12`
- termine com `!` para virar **prioridade**

O espaço é descoberto assim: se você escrever `#consultorio`, `#mac3dos`, `#pessoal`, `#estudos`, `#academia` ou `#redes`, vale o que escreveu.
Senão, se estiver dentro de um espaço, a tarefa vai para ele. Senão, o app adivinha pelas palavras (paciente, cliente, treino, aula, reels…).

### Planejar a semana (10 minutos)
No dia escolhido (domingo, por padrão, às 19h) o app lembra você e abre um passo a passo:
1. **O que ficou para trás:** escolha o destino de cada tarefa atrasada ou sem data.
2. **Prioridades da semana:** até 3 por espaço. Elas aparecem na tela Hoje, com bolinha para marcar.
3. **Quando gravar conteúdo:** escolha os dias e o horário, e o app cria as tarefas com lembrete.

### Tela limpa
Em ⚙️ → **Tela limpa**, o app esconde explicações e avisos. A tela Hoje mostra só o próximo
compromisso, as atrasadas (num botão), as 3 prioridades e as metas da semana. O resto fica num botão "Ver".

### Lembretes
- Na hora de cada tarefa: notificação + som + vibração, com botões **Feito**, **Adiar 10 min**, **Adiar 1 h** e **Focar**.
- ☀️ De manhã: lembrete para planejar o dia. 🌙 À noite: revisão do dia (passa o que ficou para amanhã).
- **Importante:** o navegador só consegue avisar enquanto o app estiver aberto ou em segundo plano.
  Para avisos garantidos **com o app fechado**, toque na tarefa → **📅 Google Agenda**, ou na tela Agenda → **Exportar**.
  A agenda do celular faz o alarme.

### Seus dados
Ficam salvos **só no seu aparelho** (nada vai para a internet). Em ⚙️ dá para **baixar um backup** e
**restaurar** (também serve para passar os dados do computador para o celular).

## Como colocar no celular

O app é publicado de graça pelo **GitHub Pages**, no endereço
**https://macedorael.github.io/Projeto-Nutri/**

### Ativar a publicação (só uma vez)
1. No GitHub, abra o repositório **Projeto-Nutri** → **Settings** → **Pages**.
2. Em **Build and deployment → Source**, escolha **GitHub Actions**.
3. Junte este ramo na `main` (botão **Merge** do pull request). A partir daí, cada mudança no
   app é publicada sozinha em 1 ou 2 minutos (veja na aba **Actions**).

### Instalar no iPhone
1. Abra **https://macedorael.github.io/Projeto-Nutri/** no **Safari** (tem que ser o Safari).
2. Toque em **Compartilhar** (quadrado com seta) → **Adicionar à Tela de Início** → **Adicionar**.
3. Abra o app **pelo ícone** na tela de início (não pelo Safari) e toque em **Ativar** no aviso de lembretes.
   As notificações só funcionam no app instalado assim (iOS 16.4 ou mais novo).

O app instalado guarda os dados separados do Safari. Use sempre o ícone da tela de início.
Para passar o que você já anotou no link de teste, use ⚙️ → **Baixar backup** lá e **Restaurar backup** aqui.

Para testar no computador: abra um terminal nesta pasta, rode `python -m http.server 8000` e acesse `http://localhost:8000`.

## Arquivos
- `index.html`: o app inteiro
- `sw.js`: faz funcionar offline e abrir o app ao tocar na notificação
- `manifest.json` e ícones: permitem instalar como aplicativo
