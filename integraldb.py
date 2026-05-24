# =====================================================
# INTEGRALDB — VERSÃO STREAMLIT
# =====================================================

import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# CONFIGURAÇÃO
# =====================================================

st.set_page_config(
    page_title="IntegralDB",
    page_icon="💾",
    layout="centered"
)

# =====================================================
# ESTILO CYBERPUNK AZUL
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #000000;
    color: #00BFFF;
}

h1, h2, h3, h4 {
    color: #00BFFF;
}

.stButton>button {
    background-color: #001133;
    color: #00BFFF;
    border: 1px solid #00BFFF;
    border-radius: 10px;
}

.stTextInput>div>div>input {
    background-color: #001133;
    color: #00BFFF;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# VARIÁVEL
# =====================================================

x = sp.symbols('x')

# =====================================================
# SESSION STATE
# =====================================================

if "fase" not in st.session_state:
    st.session_state.fase = 1

if "pontos" not in st.session_state:
    st.session_state.pontos = 0

if "vidas" not in st.session_state:
    st.session_state.vidas = 10

if "fase_liberada" not in st.session_state:
    st.session_state.fase_liberada = False

# =====================================================
# FASES
# =====================================================

fases = {

    1: {
        "nome": "CACHE DE LOGS",
        "historia":
            "Os registros do servidor principal "
            "foram parcialmente corrompidos.",

        "enunciado":
            "O sistema monitora a taxa de "
            "crescimento do armazenamento "
            "de logs ao longo do tempo.",

        "funcao": x**2,

        "a": 0,
        "b": 2,

        "pergunta":
            "Calcule a quantidade total "
            "de dados acumulados entre "
            "0h e 2h.",

        "pontos": 100
    },

    2: {
        "nome": "TABELAS FRAGMENTADAS",

        "historia":
            "Fragmentos do banco precisam "
            "ser reconstruídos.",

        "enunciado":
            "A taxa de recuperação de dados "
            "das tabelas é dada pela função:",

        "funcao": 3*x**2 + 5,

        "a": 1,
        "b": 3,

        "pergunta":
            "Determine o total de registros "
            "recuperados entre 1h e 3h.",

        "pontos": 150
    },

    3: {
        "nome": "FIREWALL MATEMÁTICO",

        "historia":
            "Um firewall inteligente bloqueia "
            "o acesso ao núcleo do sistema.",

        "enunciado":
            "A taxa de tráfego de pacotes "
            "recebidos pelo firewall é:",

        "funcao": 3/x + x**2,

        "a": 1,
        "b": 2,

        "pergunta":
            "Calcule o total de pacotes "
            "processados pelo firewall.",

        "pontos": 250
    },

    4: {
        "nome": "NÚCLEO DE DESCRIPTOGRAFIA",

        "historia":
            "A criptografia do sistema usa "
            "integração por substituição.",

        "enunciado":
            "A taxa de descriptografia "
            "dos dados é modelada por:",

        "funcao": 2*x*(x**2 + 1)**5,

        "a": 0,
        "b": 1,

        "pergunta":
            "Determine o volume total "
            "de dados descriptografados.",

        "pontos": 500,

        "substituicao": True,

        "u_correto": "x**2 + 1"
    },

    5: {
        "nome": "MAINFRAME CENTRAL",

        "historia":
            "O núcleo do servidor requer "
            "integração por partes.",

        "enunciado":
            "A taxa de sincronização "
            "dos processos do mainframe é:",

        "funcao": x*sp.exp(x),

        "a": 0,
        "b": 1,

        "pergunta":
            "Calcule o total de processos "
            "sincronizados.",

        "pontos": 1000,

        "partes": True,

        "u_correto": "x",

        "dv_correto": "exp(x)"
    },

    6: {
        "nome": "EXPANSÃO DE CACHE",

        "historia":
            "O cache distribuído da rede "
            "está crescendo rapidamente.",

        "enunciado":
            "A taxa de crescimento do cache "
            "de consultas do banco é:",

        "funcao": -0.005*x**2 + 0.2*x + 1.5,

        "a": 6,
        "b": 18,

        "pergunta":
            "Determine o crescimento total "
            "do cache entre 6h e 18h.",

        "pontos": 350
        "taxa": True,
        "variavel": "D"
    },

    7: {
        "nome": "TRÁFEGO DO FIREWALL",

        "historia":
            "O sistema detectou um ataque "
            "cibernético massivo.",

        "enunciado":
            "A taxa de entrada de pacotes "
            "no firewall é dada por:",

        "funcao": -0.01*x**2 + 0.18*x + 2,

        "a": 4,
        "b": 16,

        "pergunta":
            "Calcule o total de pacotes "
            "recebidos durante o ataque.",

        "pontos": 400
    },

    8: {
        "nome": "BACKUP AUTOMÁTICO",

        "historia":
            "O sistema iniciou um backup "
            "de emergência.",

        "enunciado":
            "A velocidade de transferência "
            "de dados do backup é:",

        "funcao": 0.5*x + 3,

        "a": 2,
        "b": 8,

        "pergunta":
            "Determine o volume total "
            "de dados transferidos.",

        "pontos": 450
    },

    9: {
        "nome": "INGESTÃO BIG DATA",

        "historia":
            "A IA central está absorvendo "
            "dados exponencialmente.",

        "enunciado":
            "A taxa de ingestão de dados "
            "do sistema de IA é dada por:",

        "funcao": 4*sp.exp(0.1*x),

        "a": 0,
        "b": 5,

        "pergunta":
            "Calcule a quantidade total "
            "de dados ingeridos pelo sistema.",

        "pontos": 700
    },

    10: {
        "nome": "SINCRONIZAÇÃO DE SERVIDORES",

        "historia":
            "Dois servidores da corporação "
            "processam pacotes simultaneamente.",

        "enunciado":
            "A taxa de processamento do "
            "Servidor A e do Servidor B "
            "é modelada pelas funções:",

        "funcao1": -0.1*x**2 + 2*x + 5,

        "funcao2": 0.5*x + 2,

        "a": 0,
        "b": 10,

        "pergunta":
            "Calcule a área entre as duas "
            "funções no intervalo dado.",

        "pontos": 300,

        "duas_funcoes": True
    }
}

# =====================================================
# GAME OVER
# =====================================================

if st.session_state.vidas <= 0:

    st.error("☠️ SISTEMA COMPROMETIDO")
    st.stop()

# =====================================================
# FINAL
# =====================================================

if st.session_state.fase > len(fases):

    st.success("👑 MAINFRAME RESTAURADO")

    st.write(
        f"Pontuação Final: "
        f"{st.session_state.pontos}"
    )

    st.balloons()

    st.stop()

# =====================================================
# FASE ATUAL
# =====================================================

fase = fases[st.session_state.fase]

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("💾 STATUS")

st.sidebar.metric(
    "Fase",
    st.session_state.fase
)

st.sidebar.metric(
    "Pontos",
    st.session_state.pontos
)

st.sidebar.metric(
    "Vidas",
    st.session_state.vidas
)

# =====================================================
# TÍTULO
# =====================================================

st.title("💾 INTEGRALDB")

st.subheader(
    f"🔥 FASE {st.session_state.fase} — "
    f"{fase['nome']}"
)

# =====================================================
# HISTÓRIA
# =====================================================

st.write(fase["historia"])

# =====================================================
# ENUNCIADO
# =====================================================

st.write(fase["enunciado"])

# =====================================================
# INTEGRAL
# =====================================================

# =====================================================
# EXPRESSÕES MATEMÁTICAS
# =====================================================

# =====================================================
# ÁREA ENTRE CURVAS
# =====================================================

if "duas_funcoes" in fase:

    st.latex(
        "f(x)="
        + sp.latex(fase["funcao1"])
    )

    st.latex(
        "g(x)="
        + sp.latex(fase["funcao2"])
    )

    st.write(
        "Considere o intervalo:"
    )

    st.latex(
        f"{fase['a']} \\leq x \\leq {fase['b']}"
    )

# =====================================================
# QUESTÕES DE TAXA
# =====================================================

elif "taxa" in fase:

    variavel = fase.get(
        "variavel",
        "D"
    )

    st.latex(
        rf"\frac{{d{variavel}}}{{dt}}="
        + sp.latex(fase["funcao"])
    )

# =====================================================
# QUESTÕES NORMAIS
# =====================================================

else:

    st.latex(
        sp.latex(
            sp.Integral(
                fase["funcao"],
                (x, fase["a"], fase["b"])
            )
        )
    )

# =====================================================
# PERGUNTA
# =====================================================

st.write(fase["pergunta"])

# =====================================================
# GRÁFICO
# =====================================================

if "duas_funcoes" in fase:

    f1 = sp.lambdify(
        x,
        fase["funcao1"],
        "numpy"
    )

    f2 = sp.lambdify(
        x,
        fase["funcao2"],
        "numpy"
    )

    x_vals = np.linspace(
        fase["a"],
        fase["b"],
        400
    )

    y1 = f1(x_vals)
    y2 = f2(x_vals)

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(
        x_vals,
        y1,
        label="Servidor A"
    )

    ax.plot(
        x_vals,
        y2,
        label="Servidor B"
    )

    ax.fill_between(
        x_vals,
        y1,
        y2,
        alpha=0.3
    )

    ax.legend()

    ax.grid()

    ax.set_title(
        "Área Entre as Curvas"
    )

    st.pyplot(fig)

else:

    f = sp.lambdify(
        x,
        fase["funcao"],
        "numpy"
    )

    x_vals = np.linspace(
        fase["a"],
        fase["b"],
        400
    )

    y_vals = f(x_vals)

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(x_vals, y_vals)

    ax.fill_between(
        x_vals,
        y_vals,
        alpha=0.3
    )

    ax.grid()

    ax.set_title(
        "Área Sob a Curva"
    )

    st.pyplot(fig)

# =====================================================
# SUBSTITUIÇÃO
# =====================================================

escolha_u = None

if "substituicao" in fase:

    escolha_u = st.radio(
        "Escolha u:",
        [
            "x**2 + 1",
            "2*x",
            "x**5"
        ]
    )

# =====================================================
# POR PARTES
# =====================================================

escolha_u_partes = None
escolha_dv = None

if "partes" in fase:

    escolha_u_partes = st.radio(
        "Escolha u:",
        [
            "x",
            "exp(x)"
        ]
    )

    escolha_dv = st.radio(
        "Escolha dv:",
        [
            "x",
            "exp(x)"
        ]
    )
    
# =====================================================
# INPUT
# =====================================================

resposta = st.text_input(
    "Digite sua resposta:"
)

# =====================================================
# BOTÃO
# =====================================================

if not st.session_state.fase_liberada:

    if st.button("Enviar"):

        try:

            # =================================================
            # TRATAMENTO DA RESPOSTA
            # =================================================

            resposta = (
                resposta
                .replace(",", ".")
                .replace("^", "**")
            )

            resposta_usuario = round(
                float(
                    sp.sympify(resposta)
                ),
                2
            )

            # =================================================
            # ÁREA ENTRE CURVAS
            # =================================================

            if "duas_funcoes" in fase:

                valor_correto = round(
                    float(
                        sp.integrate(
                            fase["funcao1"]
                            - fase["funcao2"],
                            (
                                x,
                                fase["a"],
                                fase["b"]
                            )
                        )
                    ),
                    2
                )

            else:

                valor_correto = round(
                    float(
                        sp.integrate(
                            fase["funcao"],
                            (
                                x,
                                fase["a"],
                                fase["b"]
                            )
                        )
                    ),
                    2
                )

            correto = abs(
                resposta_usuario
                - valor_correto
            ) < 0.1

            # =================================================
            # SUBSTITUIÇÃO
            # =================================================

            if "substituicao" in fase:

                correto = (
                    correto and
                    escolha_u
                    == fase["u_correto"]
                )

            # =================================================
            # POR PARTES
            # =================================================

            if "partes" in fase:

                correto = (
                    correto and
                    escolha_u_partes
                    == fase["u_correto"]
                    and
                    escolha_dv
                    == fase["dv_correto"]
                )

            # =================================================
            # RESULTADO
            # =================================================

            if correto:

                st.success(
                    "✅ ÁREA DESCRIPTOGRAFADA"
                )

                st.session_state.pontos += (
                    fase["pontos"]
                )

                st.session_state.fase_liberada = True

            else:

                st.error(
                    "❌ CÁLCULO INCORRETO"
                )

                st.session_state.vidas -= 1

        except:

            st.warning(
                "⚠️ Expressão inválida."
            )

# =====================================================
# PRÓXIMA FASE
# =====================================================

if st.session_state.fase_liberada:

    if st.button("🚀 Próxima Fase"):

        st.session_state.fase += 1

        st.session_state.fase_liberada = False

        st.rerun()
