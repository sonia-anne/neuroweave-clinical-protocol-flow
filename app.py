import streamlit as st
import graphviz
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

# --- STREAMLIT CONFIG ---
st.set_page_config(page_title="NEUROWEAVE - Clinical Protocol Flow", layout="wide")
st.markdown("<h1 style='text-align: center;'>🧠 NEUROWEAVE: Full Clinical Protocol Flowchart</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>A scientific visualization of the nanobot's behavior in real clinical phases – from injection to self-destruction and monitoring.</p>", unsafe_allow_html=True)

# --- 1. MAIN FLOW (GRAPHVIZ) ---
st.markdown("## 📌 Clinical Flowchart with Medical AI (Graphviz)")

dot = graphviz.Digraph()
dot.attr(rankdir='LR', size='12')

nodes = {
    "A": "💉 Injection",
    "B": "PEG Coating\nImmune Evasion",
    "C": "Magnetic Navigation",
    "D": "Blood-Brain Barrier Crossing",
    "E": "Ventricle Mapping",
    "F": "✂️ Blockage Clearance",
    "G": "Sensor Check\n(ICP, pH, Flow)",
    "H": "BDNF/VEGF Release",
    "I": "Ependymal Regeneration",
    "J": "⏳ Self-Destruction (72h)",
    "K": "📡 External Patch Monitoring",
    "L": "📊 AI Dashboard & Alerts"
}
for key, label in nodes.items():
    dot.node(key, label, shape="box", style="filled", color="deepskyblue")

edges = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), 
         ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"), ("J", "K"), ("K", "L")]
for src, tgt in edges:
    dot.edge(src, tgt)

st.graphviz_chart(dot)

# --- 2. BOTTLENECK ANALYSIS ---
st.markdown("## ⚠️ Protocol Bottleneck Points (NetworkX)")
G = nx.DiGraph()
for src, tgt in edges:
    G.add_edge(nodes[src], nodes[tgt])

fig, ax = plt.subplots(figsize=(13, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=2600,
        font_size=9, font_weight='bold', edge_color='gray', ax=ax)
st.pyplot(fig)

# --- 3. CLINICAL TIMELINE (Plotly) ---
st.markdown("## 🕒 Clinical Timeline of Each Phase (Plotly)")
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

# --- 4. SENSOR HEATMAP ---
st.markdown("## 🔥 Priority of Clinical Sensors (Heatmap)")
sensor_data = pd.DataFrame({
    "Sensors": ["ICP", "Flow", "pH Trigger", "O2 Levels", "Molecular Signals"],
    "Priority": [9.5, 8.7, 9.1, 7.5, 8.9]
})
fig_heatmap = go.Figure(data=go.Heatmap(
    z=[sensor_data["Priority"]],
    x=sensor_data["Sensors"],
    y=["Priority Index"],
    colorscale="YlOrBr"
))
fig_heatmap.update_layout(title="Sensor Priority Heatmap", height=300)
st.plotly_chart(fig_heatmap, use_container_width=True)

# --- 5. QUANTUM DECISION SIMULATION ---
st.markdown("## 🔺 Quantum-Based AI Decision Logic (Graphviz)")
q = graphviz.Digraph()
q.attr('node', shape='ellipse', style='filled', color='mediumorchid')
q.edge("START", "HIGH ICP", label="> Threshold")
q.edge("START", "NORMAL", label="≤ Threshold")
q.edge("HIGH ICP", "Enzyme Release")
q.edge("NORMAL", "Regeneration")
q.edge("Enzyme Release", "Regeneration")
q.edge("Regeneration", "Self-Destruct")
st.graphviz_chart(q)

# --- FOOTER ---
st.markdown("---")
st.success("This protocol flow represents every step in the NEUROWEAVE nanobot's medical action: from immunological evasion and AI navigation to real-time regeneration, monitoring, and ethical self-destruction.")
st.markdown("<p style='text-align: center; font-size: 14px;'>Designed by Sonia Annette Echeverría Vera – Ecuadorian Young Scientist | UNESCO-Al Fozan Candidate</p>", unsafe_allow_html=True)