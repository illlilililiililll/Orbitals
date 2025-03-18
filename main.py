import util
import Orbital
import streamlit as st

st.sidebar.markdown("## Parameters")
N = st.sidebar.number_input('Vertex', 1, 300, 50, 10)
r = st.sidebar.slider('Range', 10, 50, 20, 10)

st.sidebar.markdown("--------")
st.sidebar.markdown("## Orbital Settings")
# n = st.sidebar.selectbox('$ n $', (1, 2, 3))
n = st.sidebar.radio("$ n $", (1, 2, 3))

l_options = ['0 ($s$)', '1 ($p$)', '2 ($d$)']
# l = st.sidebar.selectbox('$ l $', p_[:n])
l = st.sidebar.radio("$ l $", l_options[:n])
l_ = int(l[0])

ml_map = {
    (1, 0): ["$1s$"],
    (2, 0): ["$2s$"],
    (2, 1): ["$2p_x$", "$2p_y$", "$2p_z$"],
    (3, 0): ["$3s$"],
    (3, 1): ["$3p_x$", "$3p_y$", "$3p_z$"],
    (3, 2): ["$3d_{xy}$", "$3d_{yz}$", "$3d_{z^2}$", "$3d_{xz}$", "$3d_{x^2-y^2}$"]
}
ml_options = ml_map.get((n, l_), [])

function_map = {
    "$1s$": "s",
    "$2s$": "s",
    "$3s$": "s",
    "$2p_x$": "px",
    "$2p_y$": "py",
    "$2p_z$": "pz",
    "$3p_x$": "px",
    "$3p_y$": "py",
    "$3p_z$": "pz",
    "$3d_{xy}$": "dxy",
    "$3d_{yz}$": "dyz",
    "$3d_{z^2}$": "dz2",
    "$3d_{xz}$": "dxz",
    "$3d_{x^2-y^2}$": "dx2y2"
}

m_l = st.sidebar.radio("$ m_l $", ml_options)

# print(f"_{n}{l_options[l_][-3]}")
orbital = Orbital.Orbital(getattr(Orbital.R, f'_{n}{l_options[l_][-3]}'), getattr(Orbital.Y, f'{function_map[m_l]}'))

st.title(f"{m_l} Orbital")
st.plotly_chart(util.plot(orbital, N, r), use_container_width=True)