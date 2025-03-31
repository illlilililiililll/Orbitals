import util
import Orbital
import streamlit as st

st.sidebar.markdown("## Parameters")
N = st.sidebar.slider('Vertex', 20, 300, 20, 10)
# r = 100 - st.sidebar.slider('Density', 0, 100, 10, 1)

st.sidebar.markdown("--------")
st.sidebar.markdown("## Orbital Settings")
n = st.sidebar.radio("$ n $", (1, 2, 3, 4, 5))

l_options = ['0 ($s$)', '1 ($p$)', '2 ($d$)', '3 ($f$)', '4 ($g$)']
# l = st.sidebar.selectbox('$ l $', p_[:n])
l = st.sidebar.radio("$ l $", l_options[:n])
l_ = int(l[0])

ml_map = {
    (1, 0): ["$1s$"],
    (2, 0): ["$2s$"],
    (2, 1): ["$2p_x$", "$2p_y$", "$2p_z$"],
    (3, 0): ["$3s$"],
    (3, 1): ["$3p_x$", "$3p_y$", "$3p_z$"],
    (3, 2): ["$3d_{xy}$", "$3d_{yz}$", "$3d_{z^2}$", "$3d_{xz}$", "$3d_{x^2-y^2}$"],
    (4, 0): ["$4s$"],
    (4, 1): ["$4p_x$", "$4p_y$", "$4p_z$"],
    (4, 2): ["$4d_{xy}$", "$4d_{yz}$", "$4d_{z^2}$", "$4d_{xz}$", "$4d_{x^2-y^2}$"],
    (4, 3): ["$4f_{xyz}$", "$4f_{yz^2}$", "$4f_{xz^2}$", "$4f_{z^3}$", "$4f_{x(x^2-3y^2)}$", "$4f_{y(3x^2-y^2)}$", "$4f_{z(x^2-y^2)}$"],
    (5, 0): ["$5s$"],
    (5, 1): ["$5p_x$", "$5p_y$", "$5p_z$"],
    (5, 2): ["$5d_{xy}$", "$5d_{yz}$", "$5d_{z^2}$", "$5d_{xz}$", "$5d_{x^2-y^2}$"],
    (5, 3): ["$5f_{xyz}$", "$5f_{yz^2}$", "$5f_{xz^2}$", "$5f_{z^3}$", "$5f_{x(x^2-3y^2)}$", "$5f_{y(3x^2-y^2)}$", "$5f_{z(x^2-y^2)}$"],
    (5, 4): ["$5g_{z^4}$", "$5g_{z^3y}$", "$5g_{z^3x}$", "$5g_{z^2xy}$", "$5g_{z^2(x^2-y^2)}$", "$5g_{zy^3}$", "$5g_{zx^3}$", "$5g_{xy(x^2-y^2)}$", "$5g_{x^4+y^4}$"]
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
    "$3d_{x^2-y^2}$": "dx2y2", 
    "$4s$": "s",
    "$4p_x$": "px",
    "$4p_y$": "py",
    "$4p_z$": "pz",
    "$4d_{xy}$": "dxy",
    "$4d_{yz}$": "dyz",
    "$4d_{z^2}$": "dz2",
    "$4d_{xz}$": "dxz",
    "$4d_{x^2-y^2}$": "dx2y2",
    "$4f_{xyz}$": "fxyz",
    "$4f_{yz^2}$": "fyz2",
    "$4f_{xz^2}$": "fxz2",
    "$4f_{z^3}$": "fz3",
    "$4f_{x(x^2-3y^2)}$": "fxx23y2",
    "$4f_{z(x^2-y^2)}$": "fzx2y2",
    "$4f_{y(3x^2-y^2)}$": "fy3x2y2",
    "$5s$": "s",
    "$5p_x$": "px",
    "$5p_y$": "py",
    "$5p_z$": "pz",
    "$5d_{xy}$": "dxy",
    "$5d_{yz}$": "dyz",
    "$5d_{z^2}$": "dz2",
    "$5d_{xz}$": "dxz",
    "$5d_{x^2-y^2}$": "dx2y2",
    "$5f_{xyz}$": "fxyz",
    "$5f_{yz^2}$": "fyz2",
    "$5f_{xz^2}$": "fxz2",
    "$5f_{z^3}$": "fz3",
    "$5f_{x(x^2-3y^2)}$": "fxx23y2",
    "$5f_{z(x^2-y^2)}$": "fzx2y2",
    "$5f_{y(3x^2-y^2)}$": "fy3x2y2",
    "$5g_{z^4}$": "gz4",
    "$5g_{z^3y}$": "gz3y",
    "$5g_{z^3x}$": "gz3x",
    "$5g_{z^2xy}$": "gz2xy",
    "$5g_{z^2(x^2-y^2)}$": "gz2x2y2",
    "$5g_{zy^3}$": "gzy3",
    "$5g_{zx^3}$": "gzx3",
    "$5g_{xy(x^2-y^2)}$": "gxyx2y2",
    "$5g_{x^4+y^4}$": "gx4y4"
}

m_l = st.sidebar.radio("$ m_l $", ml_options)

# print(f"_{n}{l_options[l_][-3]}")
orbital = Orbital.Orbital(getattr(Orbital.R, f'_{n}{l_options[l_][-3]}'), getattr(Orbital.Y, f'{function_map[m_l]}'))

st.title(f"{m_l} Orbital")
st.plotly_chart(util.plot(orbital, N, max(n**2, 10)), use_container_width=True)