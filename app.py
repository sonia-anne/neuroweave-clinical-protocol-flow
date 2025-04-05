import streamlit as st
import graphviz
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

# --- STREAMLIT CONFIG ---
st.set_page_config(page_title="NEUROWEAVE - Intelligent Clinical Flow", layout="wide", page_icon="🧠")
st.title("🧠 NEUROWEAVE - Intelligent Clinical Flow Diagram")
st.markdown("#### Visualizing the complete clinical journey of the NEUROWEAVE nanobot — from injection to self-destruction and monitoring — using AI and real-world protocols.")

# --- GRAPHVIZ FLOW ---
st.header("🚀 Intelligent Clinical Protocol (Graphviz)")
flow = graphviz.Digraph()
flow.attr(rankdir='LR', size='15', bgcolor='white')

steps = {
    "A": "💉 Injection",
    "B": "PEG Coating\nImmune Camouflage",
    "C": "Magnetic Navigation",
    "D": "Crossing Blood-Brain Barrier",
    "E": "3D Ventricle Mapping",
    "F": "✂️ Obstruction Removal",
    "G": "Sensor Diagnostics:\nICP, Flow, pH",
    "H": "BDNF/VEGF Release",
    "I": "Ependymal Regeneration",
    "J": "⏳ Self-Destruction",
    "K": "📡 Patch Monitoring",
    "L": "📊 AI Medical Dashboard"
}

for key, label in steps.items():
    flow.node(key, label, shape="box", style="filled", color="#bae6fd")

connections = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"), ("J", "K"), ("K", "L")]
for s, t in connections:
    flow.edge(s, t, color="#0ea5e9")

st.graphviz_chart(flow, use_container_width=True)

# --- NETWORKX BOTTLENECK ANALYSIS ---
st.header("⚠️ Bottleneck and Pathway Dependency (NetworkX)")

G = nx.DiGraph()
for src, dst in connections:
    G.add_edge(steps[src], steps[dst])

fig, ax = plt.subplots(figsize=(14, 7))
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, node_color="#bbf7d0", node_size=2500, font_size=9, edge_color="#94a3b8", font_weight="bold", ax=ax)
st.pyplot(fig)

# --- TIMELINE CHART ---
st.header("⏱️ Timeline of NEUROWEAVE Clinical Phases")

timeline_data = pd.DataFrame({
    "Step": list(steps.values()),
    "Time (hours)": [0.1, 0.3, 0.6, 1.0, 1.5, 3, 4, 24, 48, 72, 96, 120]
})

timeline_fig = go.Figure()
timeline_fig.add_trace(go.Scatter(
    x=timeline_data["Time (hours)"],
    y=timeline_data["Step"],
    mode="lines+markers",
    marker=dict(size=10, color="gold"),
    line=dict(width=3, color="royalblue")
))
timeline_fig.update_layout(
    title="NEUROWEAVE Timeline: Step-by-Step Healing Journey",
    xaxis_title="Time (hours)",
    yaxis_title="Clinical Action",
    template="plotly_white",
    height=800
)
st.plotly_chart(timeline_fig, use_container_width=True)

# --- SENSOR PRIORITY HEATMAP ---
st.header("🔥 Clinical Sensor Importance Heatmap")
sensor_df = pd.DataFrame({
    "Sensor": ["ICP", "Flow Rate", "pH Trigger", "O2 Levels", "Neural Signals"],
    "Priority": [9.6, 8.8, 9.3, 7.9, 9.0]
})

heatmap_fig = go.Figure(data=go.Heatmap(
    z=[sensor_df["Priority"]],
    x=sensor_df["Sensor"],
    y=["Priority"],
    colorscale="Turbo"
))
heatmap_fig.update_layout(
    title="Sensor Activation Priority Map",
    height=300,
    margin=dict(l=20, r=20, t=50, b=20)
)
st.plotly_chart(heatmap_fig, use_container_width=True)

# --- FOOTER ---
st.success("This intelligent flow integrates immunoengineering, fluid dynamics, neuroregeneration, and AI diagnostics — all orchestrated through NEUROWEAVE.")