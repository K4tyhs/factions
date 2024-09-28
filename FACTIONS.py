import streamlit as st
import random

if 'pontosJogador' not in st.session_state:
    st.session_state.pontosJogador = 0
if 'computador' not in st.session_state:
    st.session_state.computador = 0
if 'rodadas' not in st.session_state:
    st.session_state.rodadas = 0
if 'escolha_jogador' not in st.session_state:
    st.session_state.escolha_jogador = None
if 'escolha_computador' not in st.session_state:
    st.session_state.escolha_computador = None
if 'jogo_ativo' not in st.session_state:
    st.session_state.jogo_ativo = False
if 'escolha_desempate_jogador' not in st.session_state:
    st.session_state.escolha_desempate_jogador = None
if 'escolha_desempate_computador' not in st.session_state:
    st.session_state.escolha_desempate_computador = None
if 'desempate_ativo' not in st.session_state:
    st.session_state.desempate_ativo = False

factions = {
    1: "💥 Resistência Humana",
    2: "🤖 Drones de Combate",
    3: "🦾 Ciborgues Rebeldes",
    4: "⚙️ Unidade de Extermínio",
    5: "🧠 IA Autônoma",
    6: "🛡️ Androides Defensores",
    7: "🔋 Núcleo de Controle",
    8: "🔧 Sobreviventes Modificados",
    9: "⛏️ Robôs Mineradores",
    10: "🎯 Esquadrões de Vigilância",
    11: "🔍 Máquinas de Reconhecimento",
    12: "🚨 Sentinelas de Guerra",
    13: "🧬 Soldados Biomecânicos",
    14: "💻 Inteligência Quântica",
    15: "🚔 Patrulha Autônoma",
    16: "♻️ Unidade de Reprogramação",
    17: "💣 Tropas Cibernéticas",
    18: "🛠️ Legião da IA"
}


victories = {
    1: [7, 16, 10], 
    2: [4, 13],
    3: [3],
    4: [16],
    5: [1, 17],
    6: [6],
    7: [2, 12, 16],
    8: [1, 7, 10, 12],
    9: [7, 12, 18],
    10: [5, 14, 18],
    11: [10],
    12: [1, 2, 10, 13, 16],
    13: [8, 7, 9, 17, 18],
    14: [9, 6, 15],
    15: [5, 9, 10],
    16: [2, 8, 13],
    17: [2, 3, 5],
    18: [4, 8, 12]
}

def rodada_desempate():
    st.write("⚔️ **Rodada de Desempate: Pedra, Papel ou Tesoura** ⚔️")
    
    if not st.session_state.escolha_desempate_jogador:
        if st.button("Escolher Pedra ⚒️"):
            st.session_state.escolha_desempate_jogador = 1
        elif st.button("Escolher Papel 📜"):
            st.session_state.escolha_desempate_jogador = 2
        elif st.button("Escolher Tesoura ✂️"):
            st.session_state.escolha_desempate_jogador = 3

    # Mostra escolha do jogador e depois do computador
    if st.session_state.escolha_desempate_jogador:
        opções = {1: "Pedra ⚒️", 2: "Papel 📜", 3: "Tesoura ✂️"}
        st.write(f"🔢 Você escolheu: {opções.get(st.session_state.escolha_desempate_jogador)}")

        if not st.session_state.escolha_desempate_computador:
            st.session_state.escolha_desempate_computador = random.randint(1, 3)
            st.write(f"💻 Computador está escolhendo...")

        if st.session_state.escolha_desempate_computador:
            st.write(f"💻 Computador escolheu: {opções.get(st.session_state.escolha_desempate_computador)}")

            # Determinar o vencedor do desempate
            if st.session_state.escolha_desempate_jogador == st.session_state.escolha_desempate_computador:
                st.write("🔄 Empate no desempate!")
            elif (st.session_state.escolha_desempate_jogador == 1 and st.session_state.escolha_desempate_computador == 3) or \
                (st.session_state.escolha_desempate_jogador == 2 and st.session_state.escolha_desempate_computador == 1) or \
                (st.session_state.escolha_desempate_jogador == 3 and st.session_state.escolha_desempate_computador == 2):
                st.write("🏆 Você venceu o desempate!")
                st.session_state.pontosJogador += 1
            else:
                st.write("🥺 Computador venceu o desempate!")
                st.session_state.computador += 1

        # Reset das escolhas de desempate
        st.session_state.escolha_desempate_jogador = None
        st.session_state.escolha_desempate_computador = None
        st.session_state.desempate_ativo = False


st.title("🤖 Bem-vindo(a) ao Mundo Dominado pela IA ")

# Menu da barra lateral 
st.sidebar.subheader("Facções de Sobrevivência e IA:")
for num, faccao in factions.items():
    st.sidebar.write(f"{num} - {faccao}")

st.sidebar.markdown("---")
st.sidebar.write(f"**Rodadas:** {st.session_state.rodadas}/10")
st.sidebar.write(f"**Seus Pontos:** {st.session_state.pontosJogador}")
st.sidebar.write(f"**Pontos do Computador:** {st.session_state.computador}")

# Botão para iniciar o jogo
if not st.session_state.jogo_ativo:
    if st.button("Iniciar Jogo"):
        st.session_state.jogo_ativo = True
        st.session_state.rodadas = 0
        st.session_state.pontosJogador = 0
        st.session_state.computador = 0
        st.session_state.escolha_jogador = None
        st.session_state.escolha_computador = None
        st.success("🤖 O jogo começou! O mundo está sob controle da IA, e a sobrevivência depende de suas decisões!")
else:
    if st.session_state.rodadas < 10:
        st.write(f"⚔️ **Rodada:** {st.session_state.rodadas + 1}/10")
        
        # Escolha do computador
        if st.session_state.escolha_computador is None:
            st.session_state.escolha_computador = random.randint(1, 18)
        tipo_comp = factions.get(st.session_state.escolha_computador, "Desconhecido")
        st.write(f"💻 **A facção do computador é:** {st.session_state.escolha_computador} - {tipo_comp}")
        
        # Entrada de número para a escolha do jogador
        st.session_state.escolha_jogador = st.number_input("Escolha a facção com que vai lutar (1-18):", min_value=1, max_value=18, step=1)
        tipo_jogador = factions.get(st.session_state.escolha_jogador, "Desconhecido")
        st.write(f"🧑‍💻 **Sua facção é:** {st.session_state.escolha_jogador} - {tipo_jogador}")
        
        # Botão de Verificação
        if st.button("Verificar"):
            if st.session_state.escolha_computador in victories:
                if st.session_state.escolha_jogador in victories[st.session_state.escolha_computador]:
                    # Casos especiais para facções como Ciborgues e Criaturas Radioativas que requerem desempate
                    if st.session_state.escolha_computador == 3 or st.session_state.escolha_computador == 6:
                        st.write(f"⚔️ Facção {tipo_comp} requer desempate!")
                        st.session_state.desempate_ativo = True
                        rodada_desempate()  # Chama o desempate
                    else:
                        st.write("🏆 Você ganhou esta rodada!")
                        st.session_state.pontosJogador += 1
                        st.session_state.rodadas += 1  # Jogador vence, então a rodada conta
                else:
                    st.write("🥺 Computador venceu esta rodada!")
                    st.session_state.computador += 1
                    # Nenhuma alteração no número de rodadas
            else:
                st.write("⚠️ Facção não mapeada para vitórias.")
            
            # Reset das escolhas após verificação
            st.session_state.escolha_computador = None
            st.session_state.escolha_jogador = None
    else:
        # Centralizando o texto e o botão
        st.markdown("<div style='text-align: center;'><h1>🤖 Você sobreviveu à IA! 🤖</h1></div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center;'><p>Você conseguiu derrotar as criações da IA e provou ser o líder da Resistência!</p></div>", unsafe_allow_html=True)

        if st.button("Jogar Novamente", key="reset"):
            st.session_state.jogo_ativo = False
            st.session_state.rodadas = 0
            st.session_state.pontosJogador = 0
            st.session_state.computador = 0
            st.experimental_rerun()
