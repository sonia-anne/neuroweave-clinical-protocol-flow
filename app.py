import streamlit as st
import graphviz
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="NEUROWEAVE Clinical Flowchart", layout="wide")
st.title("🧠 NEUROWEAVE – Full Clinical Protocol Flow")
st.markdown("An advanced scientific visualization of each clinical phase of NEUROWEAVE nanobot: from injection to regeneration and self-destruction.")

# --- SECTION 1: MAIN FLOWCHART (Graphviz) ---
st.header("📌 Intelligent Clinical Flow Diagram (Zoom Enhanced)")

dot = graphviz.Digraph()
dot.attr(rankdir='LR', size='16,12')  # Aumenta el tamaño horizontal y vertical

# Puedes cambiar también los colores para mejor contraste si deseas
for key, label in nodes.items():
    dot.node(key, label, shape="box", style="filled", color="lightblue", fontsize="20")

# Define las conexiones
for src, tgt in edges:
    dot.edge(src, tgt)

# Visualiza el diagrama en mayor resolución
st.graphviz_chart(dot, use_container_width=False)  # <-- set False para evitar escalado forzado
# --- SECTION 2: BOTTLENECK DETECTION (NetworkX) ---
st.header("⚠️ Bottleneck Analysis in Clinical Protocol")

G = nx.DiGraph()
for src, tgt in edges:
    G.add_edge(nodes[src], nodes[tgt])

fig, ax = plt.subplots(figsize=(12, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="#90ee90", node_size=2500,
        font_size=9, font_weight='bold', edge_color='gray', ax=ax)
st.pyplot(fig)

# --- SECTION 3: PHASE TIMELINE (Plotly) ---
st.header("🕒 Clinical Phase Timeline")

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
fig_timeline.update_layout(title="NEUROWEAVE Clinical Timeline",
                           xaxis_title="Time (hours)",
                           yaxis_title="Protocol Phase",
                           height=700,
                           plot_bgcolor="#0f172a",
                           paper_bgcolor="#0f172a",
                           font=dict(color="white"))
st.plotly_chart(fig_timeline, use_container_width=True)

# --- SECTION 4: SENSOR PRIORITY HEATMAP ---
st.header("🔥 Sensor Priority Heatmap")

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
fig_heatmap.update_layout(title="Sensor Activation Priority", height=300)
st.plotly_chart(fig_heatmap, use_container_width=True)

# --- SECTION 5: QUANTUM DECISION SIMULATION ---
st.header("🔺 Quantum-Level Decision Simulation")

q = graphviz.Digraph()
q.attr('node', shape='ellipse', style='filled', color='mediumpurple')
q.edge("START", "HIGH ICP", label="> Threshold")
q.edge("START", "NORMAL", label="≤ Threshold")
q.edge("HIGH ICP", "Enzyme Release")
q.edge("NORMAL", "Regeneration")
q.edge("Enzyme Release", "Regeneration")
q.edge("Regeneration", "Self-Destruct")
st.graphviz_chart(q, use_container_width=True)

# --- FOOTER ---
st.success("This diagram summarizes NEUROWEAVE’s clinical process: combining immunology, AI, magnetic navigation, regeneration, and self-controlled biodegradation.")