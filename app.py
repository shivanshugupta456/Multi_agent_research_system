import streamlit as st
import time
from pipeline import run_research_pipeline

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

/* ── Background ── */
.stApp {
    background-color: #0c0e14;
    color: #e8eaf0;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 3rem;
    max-width: 900px;
}

/* ── Hero title ── */
.hero-title {
    font-family: 'Space Mono', monospace;
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.25rem;
}
.hero-sub {
    font-size: 1rem;
    color: #6b7280;
    margin-bottom: 2.5rem;
    letter-spacing: 0.01em;
}
.accent { color: #7c6af7; }

/* ── Input area ── */
.stTextInput > div > div > input {
    background: #161922 !important;
    border: 1.5px solid #2a2d3a !important;
    border-radius: 10px !important;
    color: #e8eaf0 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.2s;
}
.stTextInput > div > div > input:focus {
    border-color: #7c6af7 !important;
    box-shadow: 0 0 0 3px rgba(124,106,247,0.15) !important;
}

/* ── Button ── */
.stButton > button {
    background: #7c6af7 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.65rem 2rem !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.9rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em !important;
    cursor: pointer !important;
    transition: background 0.2s, transform 0.1s !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: #6355d4 !important;
    transform: translateY(-1px) !important;
}

/* ── Step cards ── */
.step-card {
    background: #161922;
    border: 1.5px solid #2a2d3a;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s;
}
.step-card.active {
    border-color: #7c6af7;
    box-shadow: 0 0 0 1px rgba(124,106,247,0.25);
}
.step-card.done {
    border-color: #22c55e;
}
.step-card.idle {
    opacity: 0.5;
}

.step-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}
.step-label.active { color: #7c6af7; }
.step-label.done   { color: #22c55e; }
.step-label.idle   { color: #4b5563; }

.step-title {
    font-size: 1rem;
    font-weight: 600;
    color: #e8eaf0;
}
.step-desc {
    font-size: 0.85rem;
    color: #6b7280;
    margin-top: 0.2rem;
}

/* ── Result sections ── */
.result-block {
    background: #161922;
    border: 1.5px solid #2a2d3a;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}
.result-block h3 {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #7c6af7;
    margin-bottom: 1rem;
}
.result-block p, .result-block div {
    font-size: 0.93rem;
    line-height: 1.75;
    color: #c9ccd6;
}

/* ── Scraped content mono ── */
.mono-block {
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    line-height: 1.7;
    color: #9ca3af;
    white-space: pre-wrap;
    word-break: break-word;
    max-height: 300px;
    overflow-y: auto;
    padding: 1rem;
    background: #0c0e14;
    border-radius: 8px;
    border: 1px solid #1f2330;
}

/* ── Critic feedback ── */
.critic-block {
    background: #161922;
    border: 1.5px solid #f59e0b44;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}
.critic-block h3 {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #f59e0b;
    margin-bottom: 1rem;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #161922; }
::-webkit-scrollbar-thumb { background: #2a2d3a; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-title">Research<span class="accent">.</span>Agent</div>
<div class="hero-sub">Multi-agent pipeline — search → scrape → write → critique</div>
""", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
col_input, col_btn = st.columns([5, 1])
with col_input:
    topic = st.text_input(
        label="topic",
        placeholder="e.g. Quantum computing breakthroughs in 2025",
        label_visibility="collapsed",
    )
with col_btn:
    run = st.button("RUN →")

st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

# ── Pipeline stages config ────────────────────────────────────────────────────
STAGES = [
    ("STEP 01", "Search Agent",  "Querying the web for recent, reliable sources"),
    ("STEP 02", "Reader Agent",  "Scraping the most relevant URL for deep content"),
    ("STEP 03", "Writer Chain",  "Drafting a structured research report"),
    ("STEP 04", "Critic Chain",  "Reviewing the report and producing feedback"),
]

def render_stages(active: int = -1, done_up_to: int = -1):
    cols = st.columns(4)
    for i, (label, title, desc) in enumerate(STAGES):
        if i <= done_up_to:
            status = "done";   icon = "✓"
        elif i == active:
            status = "active"; icon = "●"
        else:
            status = "idle";   icon = "○"
        with cols[i]:
            st.markdown(f"""
            <div class="step-card {status}">
                <div class="step-label {status}">{icon} {label}</div>
                <div class="step-title">{title}</div>
                <div class="step-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


# ── Run pipeline ──────────────────────────────────────────────────────────────
if run:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    stage_placeholder = st.empty()
    status_placeholder = st.empty()

    # Stage 1 active
    with stage_placeholder.container():
        render_stages(active=0)
    status_placeholder.markdown(
        "<p style='color:#7c6af7;font-family:Space Mono,monospace;font-size:0.8rem;'>🔍 Search agent working...</p>",
        unsafe_allow_html=True
    )

    # We'll capture output progressively by monkey-patching the pipeline
    # Since pipeline prints to stdout we run it and update stages as state fills
    state = {}

    # ── Patch: run step by step via direct imports ──
    from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

    # Step 1 — Search
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state["search_results"] = search_result['messages'][-1].content

    with stage_placeholder.container():
        render_stages(active=1, done_up_to=0)
    status_placeholder.markdown(
        "<p style='color:#7c6af7;font-family:Space Mono,monospace;font-size:0.8rem;'>🌐 Reader agent scraping top resource...</p>",
        unsafe_allow_html=True
    )

    # Step 2 — Reader
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })
    state["scraped_content"] = reader_result['messages'][-1].content

    with stage_placeholder.container():
        render_stages(active=2, done_up_to=1)
    status_placeholder.markdown(
        "<p style='color:#7c6af7;font-family:Space Mono,monospace;font-size:0.8rem;'>✍️ Writer drafting the report...</p>",
        unsafe_allow_html=True
    )

    # Step 3 — Writer
    research_combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
    )
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined,
    })

    with stage_placeholder.container():
        render_stages(active=3, done_up_to=2)
    status_placeholder.markdown(
        "<p style='color:#f59e0b;font-family:Space Mono,monospace;font-size:0.8rem;'>🧐 Critic reviewing the report...</p>",
        unsafe_allow_html=True
    )

    # Step 4 — Critic
    state["feedback"] = critic_chain.invoke({"report": state["report"]})

    with stage_placeholder.container():
        render_stages(done_up_to=3)
    status_placeholder.markdown(
        "<p style='color:#22c55e;font-family:Space Mono,monospace;font-size:0.8rem;'>✓ Pipeline complete.</p>",
        unsafe_allow_html=True
    )

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.divider()
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    # ── Results ───────────────────────────────────────────────────────────────

    # Search results
    with st.expander("🔍  Search Results", expanded=False):
        st.markdown(f"""
        <div class="result-block">
            <h3>Search Results</h3>
            <div>{state['search_results']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Scraped content
    with st.expander("🌐  Scraped Content", expanded=False):
        st.markdown(f"""
        <div class="result-block">
            <h3>Scraped Content</h3>
            <div class="mono-block">{state['scraped_content']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Final report — always expanded
    st.markdown(f"""
    <div class="result-block">
        <h3>📄 Final Report — {topic}</h3>
        <div>{state['report']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Critic feedback — always expanded
    st.markdown(f"""
    <div class="critic-block">
        <h3>🧐 Critic Feedback</h3>
        <div style="font-size:0.93rem;line-height:1.75;color:#c9ccd6;">{state['feedback']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Download button
    full_output = (
        f"# Research Report: {topic}\n\n"
        f"## Report\n{state['report']}\n\n"
        f"## Critic Feedback\n{state['feedback']}\n\n"
        f"## Search Results\n{state['search_results']}\n\n"
        f"## Scraped Content\n{state['scraped_content']}"
    )
    st.download_button(
        label="⬇ Download full report (.md)",
        data=full_output,
        file_name=f"research_{topic[:40].replace(' ','_')}.md",
        mime="text/markdown",
    )

else:
    # Idle state — show all stages as inactive
    render_stages()
    st.markdown("""
    <div style="margin-top:2rem;padding:1.5rem;background:#161922;border:1.5px dashed #2a2d3a;
                border-radius:12px;text-align:center;color:#4b5563;font-size:0.9rem;line-height:1.7;">
        Enter a topic above and click <strong style="color:#7c6af7;">RUN →</strong> to start the pipeline.<br>
        The agents will search the web, scrape a source, write a report, and review it — automatically.
    </div>
    """, unsafe_allow_html=True)

