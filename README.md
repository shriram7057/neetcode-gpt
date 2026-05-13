<!-- =========================
PREMIUM GPT PROJECT WEBSITE
========================= -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>
My GPT — Built from Scratch
</title>
<!-- FONT -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<!-- ICONS -->
<script src="https://unpkg.com/lucide@latest">
</script>
<style>
:root{
--bg:#060816;
--card:#111827;
--text:#f3f4f6;
--muted:#9ca3af;
--border:rgba(255,255,255,0.08);
--primary:#60a5fa;
--secondary:#8b5cf6;
}

body.light{
--bg:#f5f7fb;
--card:#ffffff;
--text:#111827;
--muted:#4b5563;
--border:rgba(0,0,0,0.08);
}

*{
margin:0;
padding:0;
box-sizing:border-box;
}

html{
scroll-behavior:smooth;
}

body{
font-family:'Inter',sans-serif;
background:var(--bg);
color:var(--text);
overflow-x:hidden;
transition:0.3s ease;
}

/* =========================
ANIMATED BACKGROUND
========================= */

.animated-bg{
position:fixed;
inset:0;
z-index:-1;
background:
radial-gradient(circle at 20% 20%, rgba(96,165,250,0.15), transparent 25%),
radial-gradient(circle at 80% 0%, rgba(139,92,246,0.15), transparent 25%),
radial-gradient(circle at 50% 80%, rgba(59,130,246,0.12), transparent 30%);
animation:bgMove 12s ease infinite alternate;
}

@keyframes bgMove{
from{
transform:translateY(0px) scale(1);
}
to{
transform:translateY(-20px) scale(1.05);
}
}

.container{
max-width:1200px;
margin:auto;
padding:20px;
}

/* =========================
NAVBAR
========================= */

nav{
display:flex;
justify-content:space-between;
align-items:center;
padding:20px 0;
margin-bottom:40px;
}

.logo{
font-size:1.3rem;
font-weight:800;
}

.nav-actions{
display:flex;
gap:14px;
align-items:center;
}

.toggle-btn{
width:46px;
height:46px;
border-radius:12px;
border:1px solid var(--border);
background:var(--card);
color:var(--text);
cursor:pointer;
display:flex;
align-items:center;
justify-content:center;
transition:0.3s;
}

.toggle-btn:hover{
transform:translateY(-2px);
}

/* =========================
HERO
========================= */

.hero{
text-align:center;
padding:100px 20px;
}

.hero h1{
font-size:5rem;
font-weight:800;
line-height:1.1;
margin-bottom:24px;

background:linear-gradient(to right,#60a5fa,#8b5cf6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.hero p{
max-width:850px;
margin:auto;
color:var(--muted);
font-size:1.2rem;
line-height:1.8;
}

.badge{
display:inline-block;
margin-top:28px;
padding:12px 22px;
border-radius:999px;
background:rgba(96,165,250,0.1);
border:1px solid rgba(96,165,250,0.3);
color:#93c5fd;
font-weight:600;
}

.buttons{
margin-top:36px;
display:flex;
justify-content:center;
flex-wrap:wrap;
gap:16px;
}

.btn{
padding:15px 26px;
border-radius:14px;
text-decoration:none;
font-weight:600;
transition:0.3s ease;
}

.btn-primary{
background:linear-gradient(to right,#3b82f6,#8b5cf6);
color:white;
}

.btn-secondary{
background:var(--card);
color:var(--text);
border:1px solid var(--border);
}

.btn:hover{
transform:translateY(-3px);
}

/* =========================
SECTION
========================= */

section{
margin-top:100px;
}

.section-title{
font-size:2.2rem;
margin-bottom:26px;
font-weight:800;
}

.card{
background:rgba(17,24,39,0.75);
backdrop-filter:blur(18px);
border:1px solid var(--border);
border-radius:24px;
padding:34px;
transition:0.3s ease;
}

body.light .card{
background:rgba(255,255,255,0.85);
}

.card:hover{
transform:translateY(-4px);
border-color:rgba(96,165,250,0.3);
}

/* =========================
FEATURES GRID
========================= */

.grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
gap:22px;
}

.feature{
background:var(--card);
border:1px solid var(--border);
border-radius:20px;
padding:28px;
transition:0.3s ease;
}

.feature:hover{
transform:translateY(-5px);
}

.feature h3{
margin:18px 0;
font-size:1.2rem;
}

.feature ul{
padding-left:18px;
color:var(--muted);
}

.feature li{
margin-bottom:10px;
}

/* =========================
TERMINAL
========================= */

.terminal{
background:#020617;
border-radius:22px;
overflow:hidden;
border:1px solid rgba(255,255,255,0.08);
}

.terminal-top{
background:#111827;
padding:14px 18px;
display:flex;
gap:10px;
}

.dot{
width:12px;
height:12px;
border-radius:50%;
}

.red{background:#ef4444;}
.yellow{background:#f59e0b;}
.green{background:#22c55e;}

.terminal-content{
padding:28px;
font-family:monospace;
color:#cbd5e1;
min-height:140px;
font-size:1rem;
line-height:1.8;
}

/* =========================
ARCHITECTURE
========================= */

.architecture{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(180px,1fr));
gap:20px;
margin-top:30px;
}

.arch-box{
padding:26px;
border-radius:18px;
background:var(--card);
border:1px solid var(--border);
text-align:center;
transition:0.3s;
}

.arch-box:hover{
transform:scale(1.03);
}

.arch-arrow{
text-align:center;
font-size:2rem;
margin-top:10px;
color:#60a5fa;
}

/* =========================
GITHUB BADGES
========================= */

.badges{
display:flex;
flex-wrap:wrap;
gap:14px;
margin-top:20px;
}

.badges img{
border-radius:10px;
}

/* =========================
FOOTER
========================= */

footer{
margin-top:120px;
text-align:center;
color:var(--muted);
padding-bottom:60px;
}

/* =========================
MOBILE
========================= */

@media(max-width:768px){

.hero{
padding:60px 10px;
}

.hero h1{
font-size:2.8rem;
}

.hero p{
font-size:1rem;
}

.section-title{
font-size:1.7rem;
}

.buttons{
flex-direction:column;
}

.btn{
width:100%;
}
}
</style>
</head>
<body>
<div class="animated-bg">
</div>
<div class="container">
<!-- NAVBAR -->
<nav>
<div class="logo">
🧠 My GPT
</div>
<div class="nav-actions">
<button class="toggle-btn" onclick="toggleTheme()">
🌙
</button>
</div>
</nav>
<!-- HERO -->
<section class="hero">
<h1>
Built From Scratch.
</h1>
<p>
A complete GPT implementation built while mastering the internals of
transformers, attention mechanisms, tokenization, and neural networks
through the NeetCode ML course.
</p>
<div class="badge">
Built by Shriram Lahane • May 13, 2026
</div>
<div class="buttons">
<a class="btn btn-primary" href="https://neetcode.io">
🚀 NeetCode Course
</a>
<a class="btn btn-secondary" href="#">
⭐ GitHub Repository
</a>
</div>
</section>
<!-- TYPING TERMINAL -->
<section>
<h2 class="section-title">
✨ GPT Text Generation
</h2>
<div class="terminal">
<div class="terminal-top">
<div class="dot red">
</div>
<div class="dot yellow">
</div>
<div class="dot green">
</div>
</div>
<div class="terminal-content">
<span id="typing">
</span>
</div>
</div>
</section>
<!-- ARCHITECTURE -->
<section>
<h2 class="section-title">
🧠 Transformer Architecture
</h2>
<div class="architecture">
<div class="arch-box">
🔤
<br/>
<br/>
Tokenization
</div>
<div class="arch-box">
📚
<br/>
<br/>
Embeddings
</div>
<div class="arch-box">
⚡
<br/>
<br/>
Attention
</div>
<div class="arch-box">
🧠
<br/>
<br/>
Transformer
</div>
<div class="arch-box">
🤖
<br/>
<br/>
GPT Output
</div>
</div>
</section>
<!-- FEATURES -->
<section>
<h2 class="section-title">
🔥 Core Features
</h2>
<div class="grid">
<div class="feature">
<i data-lucide="brain">
</i>
<h3>
Neural Networks
</h3>
<ul>
<li>
Backpropagation
</li>
<li>
Gradient descent
</li>
<li>
MLP implementation
</li>
<li>
Loss functions
</li>
</ul>
</div>
<div class="feature">
<i data-lucide="cpu">
</i>
<h3>
Transformer Internals
</h3>
<ul>
<li>
Self-attention
</li>
<li>
Multi-head attention
</li>
<li>
KV Cache
</li>
<li>
RMS normalization
</li>
</ul>
</div>
<div class="feature">
<i data-lucide="database">
</i>
<h3>
NLP Pipeline
</h3>
<ul>
<li>
BPE tokenizer
</li>
<li>
Vocabulary generation
</li>
<li>
Dataset preparation
</li>
<li>
Preprocessing
</li>
</ul>
</div>
</div>
</section>
<!-- GITHUB STATS -->
<section>
<h2 class="section-title">
🔥 GitHub Stats &amp; Badges
</h2>
<div class="card">
<div class="badges">
<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&amp;logo=python"/>
<img src="https://img.shields.io/badge/PyTorch-DeepLearning-red?style=for-the-badge&amp;logo=pytorch"/>
<img src="https://img.shields.io/badge/Transformer-GPT-purple?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
</div>
<br/>
<br/>
<!-- Replace USERNAME -->
<img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&amp;show_icons=true&amp;theme=tokyonight" width="100%"/>
<br/>
<br/>
<img src="https://github-readme-streak-stats.herokuapp.com/?user=YOUR_USERNAME&amp;theme=tokyonight" width="100%"/>
</div>
</section>
<!-- FOOTER -->
<footer>
<p>
Built with ❤️ by
<strong>
Shriram Lahane
</strong>
</p>
<br/>
<p>
Understanding GPTs by implementing every core component manually.
</p>
</footer>
</div>
<!-- JS -->
<script>
// ICONS
lucide.createIcons();

// =========================
// DARK / LIGHT MODE
// =========================

function toggleTheme(){
document.body.classList.toggle("light");
}

// =========================
// TYPING EFFECT
// =========================

const text =
`> Initializing GPT...
> Loading tokenizer...
> Attention weights loaded.
> Transformer ready.

User:
"Explain transformers simply."

GPT:
"Transformers process language using attention mechanisms that allow words to understand context relative to other words in a sequence."`;

let i = 0;

function typingEffect(){

if(i < text.length){

document.getElementById("typing").innerHTML += text.charAt(i);

i++;

setTimeout(typingEffect, 22);
}
}

typingEffect();
</script>
</body>
</html>
