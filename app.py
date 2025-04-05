import streamlit as st
import graphviz
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURACIÓN DE STREAMLIT ---
st.set_page_config(page_title="NEUROWEAVE - Clinical Protocol Flow", layout="wide")
st.title("🧠 NEUROWEAVE - Full Clinical Protocol Flowchart")
st.markdown("Visualización científica del comportamiento del nanobot en fases clínicas reales, desde la inyección hasta su autodestrucción y monitoreo.")

# --- 1. FLUJO PRINCIPAL CON GRAPHVIZ ---
st.header("📌 Diagrama de Flujo Clínico con IA (Graphviz)")

dot = graphviz.Digraph()
dot.attr(rankdir='LR', size='12')

nodes = {
    "A": "💉 Injection",
    "B": "PEG Coating\nImmune Evasion",
    "C": "Magnetic Navigation",
    "D": "BBB Crossing",
    "E": "Ventricle Mapping",
    "F": "✂️ Clearance",
    "G": "Sensor Check: ICP, pH, Flow",
    "H": "BDNF/VEGF Release",
    "I": "Ependymal Regeneration",
    "J": "⏳ Self-Destruction (72h)",
    "K": "📡 External Patch Monitoring",
    "L": "📊 AI Medical Dashboard"
}
for key, label in nodes.items():
    dot.node(key, label, shape="box", style="filled", color="lightblue")

edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), 
         ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"), ("J", "K"), ("K", "L")]
for src, tgt in edges:
    dot.edge(src, tgt)

st.graphviz_chart(dot)

# --- 2. ANALÍTICA DE CUELLOS DE BOTELLA CON NETWORKX ---
st.header("⚠️ Cuellos de Botella del Protocolo Clínico (NetworkX)")

G = nx.DiGraph()
for src, tgt in edges:
    G.add_edge(nodes[src], nodes[tgt])

fig, ax = plt.subplots(figsize=(12, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=2500,
        font_size=9, font_weight='bold', edge_color='gray', ax=ax)
st.pyplot(fig)

# --- 3. LÍNEA DE TIEMPO DE FASES ---
st.header("🕒 Línea de Tiempo del Proceso Clínico (Plotly)")

df_timeline = pd.DataFrame({
    "Phase": list(nodes.values()),
    "Hours": [0.2, 0.5, 1, 1.5, 3, 4, 6, 24, 48, 72, 100, 120]
})
fig_timeline = go.Figure()
fig_timeline.add_trace(go.Scatter(
    x=df_timeline["Hours"],
    y=df_timeline["Phase"],
    mode="lines+markers",
    marker=dict(color='crimson', size=10),
    line=dict(color='deepskyblue', width=3)
))
fig_timeline.update_layout(title="NEUROWEAVE: Clinical Phase Timeline",
                           xaxis_title="Time (hours)",
                           yaxis_title="Clinical Phase",
                           height=700)
st.plotly_chart(fig_timeline, use_container_width=True)

# --- 4. HEATMAP DE SENSORES ---
st.header("🔥 Prioridad de Sensores Clínicos (Heatmap)")
sensor_data = pd.DataFrame({
    "Sensors": ["ICP", "Flow", "pH Trigger", "O2 Levels", "Molecular Signals"],
    "Priority": [9.5, 8.7, 9.1, 7.5, 8.9]
})
fig_heatmap = go.Figure(data=go.Heatmap(
    z=[sensor_data["Priority"]],
    x=sensor_data["Sensors"],
    y=["Priority Index"],
    colorscale="YlOrRd"
))
fig_heatmap.update_layout(title="Sensor Priority Heatmap", height=300)
st.plotly_chart(fig_heatmap, use_container_width=True)

# --- 5. SIMULACIÓN CUÁNTICA DE DECISIÓN ---
st.header("🔺 Simulación de Decisión Cuántica (Graphviz)")

q = graphviz.Digraph()
q.attr('node', shape='ellipse', style='filled', color='mediumpurple')
q.edge("START", "HIGH ICP", label="> Threshold")
q.edge("START", "NORMAL", label="≤ Threshold")
q.edge("HIGH ICP", "Enzyme Release")
q.edge("NORMAL", "Regeneration")
q.edge("Enzyme Release", "Regeneration")
q.edge("Regeneration", "Self-Destruct")
st.graphviz_chart(q)

# --- FOOTER ---
st.success("Este diagrama representa cada paso del flujo clínico de NEUROWEAVE, combinando inmunología, biofísica, IA médica, regeneración y autodestrucción controlada.")
