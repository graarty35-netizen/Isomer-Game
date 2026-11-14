"""Isomer Lab - game edukasi kimia retro pixel art (Puzzle + Quiz).
Jalankan: streamlit run app.py
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Isomer Lab", page_icon="🧪", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown("""
<style>
header,footer,#MainMenu,[data-testid="stSidebar"],[data-testid="collapsedControl"],
[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="stStatusWidget"],
[data-testid="stSidebarCollapsedControl"]{display:none!important}
.stApp{background:#d9f9fd}
.block-container{padding:0!important;max-width:100%!important}
iframe{border:0!important;width:100%}
</style>
""", unsafe_allow_html=True)

GAME_HTML = r"""
<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
<style>
:root{--cy:#19d3e6;--cl:#c9f7fc;--pk:#ff2d95;--yl:#ffe629;--ink:#1b1b2f}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{margin:0;font-family:'Press Start 2P',monospace;font-size:9px;color:var(--ink);user-select:none;touch-action:manipulation;
background:repeating-conic-gradient(#effdff 0 25%,#d3f8fd 0 50%) 0 0/24px 24px}
#app{max-width:480px;margin:0 auto;padding:8px;min-height:100vh}
.px{border:3px solid var(--ink);box-shadow:3px 3px 0 var(--ink);background:#fff}
section{display:none}
button{font-family:inherit;font-size:7px;padding:9px 4px;background:var(--cy);color:var(--ink);border:3px solid var(--ink);box-shadow:3px 3px 0 var(--ink);cursor:pointer}
button:active{transform:translate(3px,3px);box-shadow:none}
button:disabled{cursor:default}
#snd{position:fixed;top:6px;right:6px;z-index:40;background:var(--yl);padding:8px 6px}
.logo{margin:46px 0 14px;padding:22px 8px;text-align:center;background:var(--pk);color:#fff;font-size:26px;line-height:1.4;text-shadow:4px 4px 0 var(--ink)}
.logo small{display:block;color:var(--yl);font-size:8px;margin-top:10px;text-shadow:none}
#deco{display:flex;justify-content:center;gap:6px;margin-bottom:18px}
#deco i{width:30px;height:30px;border:3px solid var(--ink);font:normal 12px 'Press Start 2P',monospace;display:flex;align-items:center;justify-content:center;animation:bob 1.2s steps(2) infinite}
@keyframes bob{50%{transform:translateY(-5px)}}
.card{display:block;width:100%;text-align:left;padding:16px 12px;margin-bottom:14px;font-size:8px;line-height:1.9}
.card b{display:block;font-size:12px;margin-bottom:6px}
.c1{background:var(--cy)}.c2{background:var(--pk);color:#fff}
.tip{text-align:center;font-size:7px;line-height:1.9;margin-top:16px}
.bar{display:flex;gap:6px;margin:34px 0 8px}
.bar button{flex:none;background:#fff}
h1{flex:1;margin:0;background:var(--pk);color:#fff;text-align:center;padding:9px 4px;font-size:12px;text-shadow:2px 2px 0 var(--ink)}
.hud{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:8px}
.hud div{padding:5px 2px;text-align:center;font-size:7px;background:var(--yl)}
.hud b{display:block;font-size:11px;margin-top:4px}
#info{padding:8px;margin-bottom:8px;font-size:7px;line-height:1.7;display:flex;gap:10px;align-items:center;background:var(--cl)}
#mini{display:grid;gap:1px;flex:none;padding:3px;background:#fff;border:2px solid var(--ink)}
.m{width:9px;height:9px}.m.C{background:var(--pk)}.m.H{background:var(--cy)}.m.O{background:var(--yl);outline:1px solid var(--ink)}
#board{position:relative;margin:0 auto 8px;background:var(--cl);touch-action:none}
.cell{position:absolute;border:1px solid #92e6f0;font-size:8px;display:flex;align-items:center;justify-content:center}
.cell.Z{background:repeating-linear-gradient(45deg,#fff3a0 0 6px,#ffe629 6px 12px);color:#a06b00}
.cell.P{background:#fff;color:#079;box-shadow:inset 0 0 0 3px var(--cy)}
.cell.N{background:#ffd3ea;color:#c0156b;box-shadow:inset 0 0 0 3px var(--pk)}
.cell.I{background:#ff3b3b;color:#fff}
.cell.hint{outline:3px dashed var(--pk);outline-offset:-4px}
.t{position:absolute;display:flex;align-items:center;justify-content:center;font-size:13px;border:3px solid var(--ink);pointer-events:none;
transition:left .12s,top .12s;z-index:2;box-shadow:inset -3px -3px 0 rgba(0,0,0,.18)}
.t.C{background:var(--pk);color:#fff}.t.H{background:#fff}.t.O{background:var(--yl)}
.t.sel{outline:3px solid var(--ink);outline-offset:1px;z-index:3}
.t.sh{animation:sh .2s}@keyframes sh{25%{transform:translateX(-3px)}75%{transform:translateX(3px)}}
.fl{position:absolute;z-index:5;font-size:8px;pointer-events:none;animation:up .9s forwards;text-shadow:1px 1px 0 #fff;white-space:nowrap}
@keyframes up{to{transform:translateY(-26px);opacity:0}}
#lg{padding:8px;font-size:6px;line-height:2;background:#fff}
#lg i{display:inline-block;width:14px;height:10px;border:2px solid var(--ink);vertical-align:middle;margin-right:4px}
#hearts{display:flex;gap:4px;align-items:center;justify-content:center;background:#fff!important}
#hearts svg{filter:drop-shadow(1px 0 0 #1b1b2f) drop-shadow(-1px 0 0 #1b1b2f) drop-shadow(0 1px 0 #1b1b2f) drop-shadow(0 -1px 0 #1b1b2f)}
#qbarw{height:14px;margin-bottom:8px;background:#fff;padding:2px}
#qbar{height:100%;width:100%;background:var(--cy);transition:width 1s linear}
#qq{min-height:96px;padding:12px;font-size:10px;line-height:2;background:var(--cl);margin-bottom:10px}
#qopts button{display:block;width:100%;margin-bottom:9px;padding:13px 8px;font-size:9px;text-align:left;background:#fff}
#qopts button.ok{background:#7cff6b}#qopts button.no{background:#ff3b3b;color:#fff}
#qexp{min-height:30px;font-size:8px;line-height:1.9;margin-bottom:8px}
#qnext{display:none;width:100%;background:var(--yl);padding:12px}
#ov{position:fixed;inset:0;background:rgba(25,211,230,.88);display:none;align-items:center;justify-content:center;z-index:50;padding:14px}
#ov .box{max-width:380px;padding:16px;text-align:center;line-height:1.9;font-size:8px}
#ov h2{margin:0 0 10px;font-size:13px;color:var(--pk);text-shadow:2px 2px 0 var(--ink)}
#ov button{margin:12px 4px 0;background:var(--yl);font-size:9px;padding:11px 14px}
#lock{position:fixed;inset:0;z-index:55;display:none;background:rgba(27,27,47,.45)}
#helper{position:fixed;z-index:60;display:none;gap:6px;align-items:flex-end;animation:pop .35s steps(5)}
@keyframes pop{from{transform:scale(.2);opacity:0}}
#helper.c0{top:6px;left:6px}#helper.c1{top:6px;right:6px;flex-direction:row-reverse}
#helper.c2{bottom:6px;left:6px}#helper.c3{bottom:6px;right:6px;flex-direction:row-reverse}
#sprite{width:80px;height:85px;image-rendering:pixelated;flex:none;
filter:drop-shadow(1px 0 0 #1b1b2f) drop-shadow(-1px 0 0 #1b1b2f) drop-shadow(0 1px 0 #1b1b2f) drop-shadow(0 -1px 0 #1b1b2f)}
.bub{width:176px;padding:8px;font-size:7px;line-height:1.7;background:#fff}
#hb{display:none;margin-top:8px}#hb button{width:100%;padding:8px 3px;font-size:8px;background:var(--yl)}
</style></head><body>
<button id="snd">MUSIK OFF</button>
<div id="app">
 <section id="menu">
  <div class="logo px">ISOMER<br>LAB<small>GAME EDUKASI KIMIA</small></div>
  <div id="deco"></div>
  <button class="card c1 px" id="m1"><b>1 &bull; ISOMER PUZZLE</b>Geser balok atom C &amp; H menjadi struktur isomer. Ada katalis Pt/Ni, inhibitor merah, dan zona reaktif x2.</button>
  <button class="card c2 px" id="m2"><b>2 &bull; ISOMER QUIZ</b>Tebak nama &amp; rumus kimia. 3 nyawa, 15 detik per soal. Cepat!</button>
  <div class="tip">Musik 8-bit nonstop &bull; tombol MUSIK di pojok kanan atas</div>
 </section>
 <section id="puz">
  <div class="bar"><button id="back1">MENU</button><h1>ISOMER PUZZLE</h1></div>
  <div class="hud"><div class="px">LEVEL<b id="lv">1</b></div><div class="px">SKOR<b id="sc">0</b></div><div class="px">WAKTU<b id="tm">0</b></div><div class="px">LANGKAH<b id="mv">0</b></div></div>
  <div id="info" class="px"></div>
  <div id="board" class="px"></div>
  <div style="margin-bottom:8px"><button id="rs" style="width:100%">ULANGI LEVEL</button></div>
  <div id="lg" class="px"><i style="background:#fff;box-shadow:inset 0 0 0 2px #19d3e6"></i>Pt / <i style="background:#ffd3ea;box-shadow:inset 0 0 0 2px #ff2d95"></i>Ni katalis: balok meluncur instan<br>
  <i style="background:#ff3b3b"></i>Inhibitor: -3 detik, -15 poin<br><i style="background:#ffe629"></i>Zona reaktif x2: bonus skor<br>Tap balok / swipe untuk geser. Banyak arah? Tap balok lalu tap kotak bertanda.</div>
 </section>
 <section id="quiz">
  <div class="bar"><button id="back2">MENU</button><h1>ISOMER QUIZ</h1></div>
  <div class="hud"><div class="px" id="hearts"></div><div class="px">SKOR<b id="qs">0</b></div><div class="px">SOAL<b id="qn">1</b></div><div class="px">STREAK<b id="qk">0</b></div></div>
  <div id="qbarw" class="px"><div id="qbar"></div></div>
  <div id="qq" class="px"></div>
  <div id="qopts"></div>
  <div id="qexp"></div>
  <button id="qnext" class="px">LANJUT</button>
 </section>
</div>
<div id="ov"><div class="box px"><h2 id="ovt"></h2><div id="ovb"></div><div id="ovbs"></div></div></div>
<div id="lock"></div>
<div id="helper"><canvas id="sprite" width="16" height="17"></canvas>
 <div class="bub px"><div id="hq"></div><div id="hb"><button id="b1">+15 DETIK</button></div></div></div>
<script>
const $=s=>document.querySelector(s),COLS=8,ROWS=6,DIRS=[[0,1],[1,0],[0,-1],[-1,0]];
const B=[
['Alkana','C4H10',['Butana',['.HHHH.','HCCCCH','.HHHH.']],['Isobutana',['..HHH..','..HCH..','.HCCCH.','..HHH..']]],
['Alkena','C4H8',['1-Butena',['.HHHH.','HCCCCH','...HH.']],['2-Butena',['.HH.H.','HCCCCH','.H.HH.']]],
['Alkohol (-OH)','C3H8O',['1-Propanol',['.HHH..','HCCCOH','.HHH..']],['2-Propanol',['..H..','.HOH.','HCCCH','.HHH.']]],
['Asam karboksilat (-COOH)','C4H8O2',['Asam butanoat',['.HHHO..','HCCCCOH','.HHH...']],['Asam 2-metilpropanoat',['..HHH..','..HCO..','.HCCCOH','..HH...']]]
].map(l=>({type:l[0],f:l[1],a:{name:l[2][0],rows:l[2][1]},b:{name:l[3][0],rows:l[3][1]}}));
const LV=B.concat(B.map(l=>({...l,a:l.b,b:l.a})));
const Q=[
["Rumus molekul butana?","C4H10","C4H8","C4H6","C3H8"],
["Isobutana adalah isomer dari ...","Butana","Propana","Pentana","Etana"],
["CH3-CH(CH3)-CH3 bernama ...","2-metilpropana","Butana","Propana","2-metilbutana"],
["Isomer posisi dari 1-butena adalah ...","2-butena","Butana","Propena","Etena"],
["CH3-CH2-CH2-OH bernama ...","1-propanol","2-propanol","Propanon","Etanol"],
["Isomer posisi dari 1-propanol adalah ...","2-propanol","Etanol","Propanon","Metanol"],
["Rumus molekul propanol?","C3H8O","C3H6O","C3H8O2","C2H6O"],
["Gugus fungsi -COOH disebut gugus ...","Karboksil","Hidroksil","Karbonil","Amino"],
["Gugus fungsi -OH disebut gugus ...","Hidroksil","Karboksil","Karbonil","Eter"],
["Rumus molekul asam butanoat?","C4H8O2","C4H10O","C4H8O","C3H6O2"],
["Isomer rantai asam butanoat adalah ...","Asam 2-metilpropanoat","Asam propanoat","Asam pentanoat","Butanal"],
["Jumlah isomer rantai alkana C4H10?","2","1","3","4"],
["Jumlah isomer rantai alkana C5H12?","3","2","4","5"],
["2,2-dimetilpropana lebih dikenal sebagai ...","Neopentana","Isopentana","Isobutana","Pentana"],
["Rumus umum alkena?","CnH2n","CnH2n+2","CnH2n-2","CnHn"],
["Rumus umum alkana?","CnH2n+2","CnH2n","CnH2n-2","CnH2n+1"],
["Etanol berisomer fungsi dengan ...","Dimetil eter","Etana","Asam asetat","Etena"],
["Beda posisi gugus fungsi disebut isomer ...","Posisi","Rantai","Fungsi","Optik"],
["Beda kerangka karbon disebut isomer ...","Rantai","Posisi","Fungsi","Geometri"],
["Beda gugus fungsi disebut isomer ...","Fungsi","Rantai","Posisi","Geometri"],
["Rumus molekul 2-butena?","C4H8","C4H10","C4H6","C3H6"]];
/* ---------- AUDIO: chiptune orisinal bergroove ---------- */
const A={c:null,on:false,st:0,nt:0,id:0,
init(){if(this.c)return;this.c=new(window.AudioContext||window.webkitAudioContext)();this.m=this.c.createGain();this.m.gain.value=.25;this.m.connect(this.c.destination);
 const n=this.c.createBuffer(1,8820,44100),d=n.getChannelData(0);for(let i=0;i<8820;i++)d[i]=Math.random()*2-1;this.nb=n},
f:m=>440*2**((m-69)/12),
t(m,t,d,ty='square',v=.3){const c=this.c,o=c.createOscillator(),g=c.createGain();o.type=ty;o.frequency.value=this.f(m);
 g.gain.setValueAtTime(v,t);g.gain.exponentialRampToValueAtTime(.001,t+d);o.connect(g);g.connect(this.m);o.start(t);o.stop(t+d+.02)},
n(t,v=.1,d=.05){const c=this.c,s=c.createBufferSource(),g=c.createGain();s.buffer=this.nb;g.gain.setValueAtTime(v,t);g.gain.exponentialRampToValueAtTime(.001,t+d);s.connect(g);g.connect(this.m);s.start(t)},
kick(t){const c=this.c,o=c.createOscillator(),g=c.createGain();o.frequency.setValueAtTime(160,t);o.frequency.exponentialRampToValueAtTime(40,t+.12);
 g.gain.setValueAtTime(.7,t);g.gain.exponentialRampToValueAtTime(.001,t+.16);o.connect(g);g.connect(this.m);o.start(t);o.stop(t+.18)},
step(i,t,d){const k=i%16,r=[45,41,43,40][(i>>4)%4],BR=[0,-1,12,-1,0,-1,7,-1,0,12,-1,-1,10,-1,7,-1],
 LD=[-1,-1,-1,-1,69,-1,72,-1,76,-1,-1,-1,74,72,-1,-1];
 if(BR[k]>=0)this.t(r+BR[k],t,d*1.7,'triangle',.4);
 if(k==0||k==6||k==10)this.kick(t);
 if(k==4||k==12)this.n(t,.22,.12);
 if(k%2==0)this.n(t,.05,.03);
 if(LD[k]>=0)this.t(LD[k]+r-45,t,d*1.5,'square',.11);
 if(k%4==2)this.t(r+24+[0,3,7,10][k>>2],t,d*.8,'square',.04)},
tick(){const d=60/140/4;while(this.nt<this.c.currentTime+.25){this.step(this.st,this.nt,d);this.nt+=d;this.st++}},
play(){this.init();this.c.resume();this.on=true;this.nt=this.c.currentTime+.05;this.st=0;clearInterval(this.id);this.id=setInterval(()=>this.tick(),60)},
stop(){this.on=false;clearInterval(this.id)},
sfx(k){if(!this.c)return;const t=this.c.currentTime,s=(a,ty,v,d=.08)=>a.forEach((m,i)=>this.t(m,t+i*.06,d,ty,v));
 ({mv:()=>s([79],'square',.2,.06),bump:()=>s([40],'sawtooth',.2,.1),zap:()=>s([84,88,91],'square',.2),bad:()=>s([40,36],'sawtooth',.3,.25),
 win:()=>s([72,76,79,84,88,91],'square',.25,.15),pop:()=>s([88,95],'square',.15,.12)})[k]()}};
const upSnd=()=>$('#snd').textContent='MUSIK '+(A.on?'ON':'OFF');
$('#snd').onclick=e=>{e.stopPropagation();if(A.on)A.stop();else A.play();upSnd()};
addEventListener('click',()=>{if(!A.c){A.play();upSnd()}},{once:true});
/* ---------- UTIL ---------- */
let mode=null,ovOpen=false,helperOpen=false,hT,playing=false,qLive=false;
const fm=s=>s.replace(/(\d+)/g,'<sub>$1</sub>');
function tw(el,txt,cb,sp=26){const id=el._t=(el._t||0)+1;let i=0;el.textContent='';(function f(){if(el._t!=id)return;el.textContent=txt.slice(0,++i);if(i<txt.length)setTimeout(f,sp);else cb&&cb()})()}
function ov(t,h,bs){$('#ovt').innerHTML=t;$('#ovb').innerHTML=h;const w=$('#ovbs');w.innerHTML='';
 bs.forEach(([l,f])=>{const b=document.createElement('button');b.textContent=l;b.onclick=()=>{$('#ov').style.display='none';ovOpen=false;f()};w.appendChild(b)});
 $('#ov').style.display='flex';ovOpen=true}
function show(id){['menu','puz','quiz'].forEach(s=>$('#'+s).style.display=s==id?'block':'none');
 mode=id=='puz'?'p':id=='quiz'?'q':null;clearTimeout(hT);if(!mode){playing=false;qLive=false}else sched();scrollTo(0,0)}
/* ---------- PUZZLE ---------- */
let lv=0,score=0,time=0,moves=0,grid,sp,cd,tiles,used,tg,cell,dn=null,sel=null;
const board=$('#board');
const sig=a=>{const m=[];a.forEach((r,i)=>r.forEach((x,j)=>x&&x!='.'&&m.push([i,j,x])));
 const r0=Math.min(...m.map(x=>x[0])),c0=Math.min(...m.map(x=>x[1]));return m.map(x=>(x[0]-r0)+','+(x[1]-c0)+x[2]).sort().join('|')};
const inb=(r,c)=>r>=0&&c>=0&&r<ROWS&&c<COLS,free=(r,c)=>inb(r,c)&&!grid[r][c],at=(r,c)=>inb(r,c)?grid[r][c]:null;
const hud=()=>{$('#lv').textContent=(lv+1)+'/'+LV.length;$('#sc').textContent=score;$('#tm').textContent=time;$('#mv').textContent=moves};
const cs=()=>Math.min(52,Math.floor((Math.min(innerWidth,480)-28)/COLS));
function place(t){t.el.style.left=t.c*cell+2+'px';t.el.style.top=t.r*cell+2+'px'}
function layout(){cell=cs();board.style.width=COLS*cell+6+'px';board.style.height=ROWS*cell+6+'px';
 cd.forEach((row,r)=>row.forEach((e,c)=>Object.assign(e.style,{left:c*cell+'px',top:r*cell+'px',width:cell+'px',height:cell+'px'})));
 tiles.forEach(t=>{t.el.style.width=t.el.style.height=cell-4+'px';place(t)})}
function fl(txt,r,c,col){const d=document.createElement('div');d.className='fl';d.textContent=txt;d.style.cssText+=`left:${c*cell}px;top:${r*cell}px;color:${col}`;board.appendChild(d);setTimeout(()=>d.remove(),900)}
function startLevel(){
 const L=LV[lv],rows=L.a.rows,h=rows.length,w=rows[0].length,or=(ROWS-h)>>1,oc=(COLS-w)>>1;
 board.innerHTML='';sel=null;grid=[...Array(ROWS)].map(()=>Array(COLS).fill(null));sp=[...Array(ROWS)].map(()=>Array(COLS).fill(''));
 cd=grid.map(row=>row.map(()=>{const e=document.createElement('div');e.className='cell';board.appendChild(e);return e}));
 tiles=[];used=new Set();
 rows.forEach((s,r)=>[...s].forEach((ch,c)=>{if(ch!='.'){const el=document.createElement('div');el.className='t '+ch;el.textContent=ch;board.appendChild(el);
  const t={type:ch,r:r+or,c:c+oc,el};grid[t.r][t.c]=t;tiles.push(t)}}));
 const fr=[];grid.forEach((row,r)=>row.forEach((x,c)=>{if(!x)fr.push([r,c])}));fr.sort(()=>Math.random()-.5);
 ['P','N',...'I'.repeat(2+lv%4),...'ZZZZ'].forEach((k,i)=>{sp[fr[i][0]][fr[i][1]]=k});
 const lab={P:'Pt',N:'Ni',I:'X',Z:'x2'};
 sp.forEach((row,r)=>row.forEach((k,c)=>{if(k){cd[r][c].classList.add(k);cd[r][c].textContent=lab[k]}}));
 tg=sig(L.b.rows.map(s=>[...s]));time=110+(lv%4)*20;moves=0;playing=true;layout();
 $('#info').innerHTML=`<div id="mini"></div><div>${L.type}<br>${L.a.name} &rarr;<br><span style="color:#ff2d95">${L.b.name}</span><br>${fm(L.f)}</div>`;
 const mi=$('#mini'),tr=L.b.rows;mi.style.gridTemplateColumns=`repeat(${tr[0].length},9px)`;
 tr.forEach(s=>[...s].forEach(ch=>{const d=document.createElement('div');d.className='m '+ch;mi.appendChild(d)}));hud()}
function clearSel(){if(sel)sel.el.classList.remove('sel');sel=null;cd.forEach(r=>r.forEach(e=>e.classList.remove('hint')))}
function select(t,o){clearSel();sel=t;t.el.classList.add('sel');o.forEach(d=>cd[t.r+d[0]][t.c+d[1]].classList.add('hint'))}
function bump(t){A.sfx('bump');t.el.classList.add('sh');setTimeout(()=>t.el.classList.remove('sh'),200)}
function move(t,dr,dc){
 if(!playing||helperOpen||ovOpen)return;clearSel();
 if(!free(t.r+dr,t.c+dc))return bump(t);
 moves++;let slide=false;
 while(free(t.r+dr,t.c+dc)){
  grid[t.r][t.c]=null;t.r+=dr;t.c+=dc;grid[t.r][t.c]=t;
  const k=sp[t.r][t.c],key=t.r+','+t.c;
  if(k=='I'){score=Math.max(0,score-15);time=Math.max(1,time-3);fl('-3s -15',t.r,t.c,'#e00');A.sfx('bad');break}
  if(k=='Z'&&!used.has(key)){used.add(key);score+=20;fl('x2 +20',t.r,t.c,'#c80');A.sfx('zap')}
  if(k=='P'||k=='N'){slide=true;if(!used.has(key)){used.add(key);score+=25;fl((k=='P'?'Pt':'Ni')+'! +25',t.r,t.c,'#079');A.sfx('zap')}}
  if(!slide)break}
 place(t);if(!slide)A.sfx('mv');hud();
 if(sig(grid.map(row=>row.map(x=>x&&x.type)))==tg)setTimeout(done,250)}
const cellAt=e=>{const R=board.getBoundingClientRect();return[Math.floor((e.clientY-R.top-3)/cell),Math.floor((e.clientX-R.left-3)/cell)]};
board.onpointerdown=e=>{if(!playing||helperOpen)return;dn={rc:cellAt(e),x:e.clientX,y:e.clientY};board.setPointerCapture(e.pointerId)};
board.onpointercancel=()=>{dn=null};
board.onpointerup=e=>{if(!dn)return;const{rc,x,y}=dn;dn=null;if(!playing||helperOpen)return;
 const dx=e.clientX-x,dy=e.clientY-y,t0=at(rc[0],rc[1]);
 if(t0&&Math.hypot(dx,dy)>16){move(t0,...(Math.abs(dx)>Math.abs(dy)?[0,Math.sign(dx)]:[Math.sign(dy),0]));return}
 const[r,c]=cellAt(e);if(!inb(r,c)){clearSel();return}const u=at(r,c);
 if(u){const o=DIRS.filter(d=>free(u.r+d[0],u.c+d[1]));
  if(!o.length){clearSel();bump(u)}else if(o.length==1)move(u,o[0][0],o[0][1]);else select(u,o)}
 else if(sel&&Math.abs(sel.r-r)+Math.abs(sel.c-c)==1)move(sel,r-sel.r,c-sel.c);
 else clearSel()};
addEventListener('keydown',e=>{const i=['ArrowRight','ArrowDown','ArrowLeft','ArrowUp'].indexOf(e.key);if(i>=0&&sel&&mode=='p'){e.preventDefault();move(sel,...DIRS[i])}});
function done(){if(!playing)return;playing=false;const b=200+time*5+Math.max(0,150-moves*3),last=lv==LV.length-1;score+=b;hud();A.sfx('win');
 ov(last?'SEMUA ISOMER BERHASIL!':'ISOMER MATCH!',`${LV[lv].b.name} terbentuk.<br>Bonus +${b}<br>Skor: ${score}`,
 [[last?'MAIN LAGI':'LEVEL BERIKUT',()=>{if(last){lv=0;score=0}else lv++;startLevel()}],['MENU',()=>show('menu')]])}
$('#rs').onclick=()=>{if(!ovOpen&&!helperOpen&&mode=='p')startLevel()};
/* ---------- QUIZ ---------- */
let qs,qi,lives,qscore,streak,qt,cur=[];
const heart=f=>`<svg viewBox="0 0 7 6" width="24" height="21" shape-rendering="crispEdges" fill="${f?'#ff2d95':'#cfeaf0'}">`+
 ['.XX.XX.','XXXXXXX','XXXXXXX','.XXXXX.','..XXX..','...X...'].map((r,y)=>[...r].map((c,x)=>c=='X'?`<rect x="${x}" y="${y}" width="1" height="1"/>`:'').join('')).join('')+'</svg>';
function qhud(){$('#hearts').innerHTML=[0,1,2].map(i=>heart(i<lives)).join('');$('#qs').textContent=qscore;$('#qn').textContent=Math.min(qi+1,qs.length)+'/'+qs.length;$('#qk').textContent=streak}
function barUp(){const b=$('#qbar');b.style.width=Math.max(0,Math.min(1,qt/15))*100+'%';b.style.background=qt>8?'#19d3e6':qt>4?'#ffe629':'#ff3b3b'}
function startQuiz(){qs=[...Q].sort(()=>Math.random()-.5).slice(0,10);qi=0;lives=3;qscore=0;streak=0;nextQ()}
function nextQ(){
 if(qi>=qs.length||lives<=0)return endQuiz();
 const q=qs[qi];qLive=false;$('#qopts').innerHTML='';$('#qexp').textContent='';$('#qnext').style.display='none';qt=15;barUp();qhud();
 cur=q.slice(1).map((t,i)=>({t,ok:i==0})).sort(()=>Math.random()-.5);
 tw($('#qq'),q[0],()=>{cur.forEach(x=>{const b=document.createElement('button');b.textContent=x.t;x.b=b;b.onclick=()=>ans(x);$('#qopts').appendChild(b)});qLive=true})}
function ans(x){
 if(!qLive||helperOpen)return;qLive=false;const ok=x&&x.ok;
 cur.forEach(y=>{y.b.disabled=true;if(y.ok)y.b.classList.add('ok')});
 if(x&&!ok)x.b.classList.add('no');
 let msg;
 if(ok){const g=100+Math.round(qt)*5+streak*10;qscore+=g;streak++;A.sfx('zap');msg=`BENAR! +${g}`}
 else{lives--;streak=0;A.sfx('bad');msg=(x?'SALAH. ':'WAKTU HABIS. ')+'Jawaban: '+cur.find(y=>y.ok).t}
 qi++;qhud();tw($('#qexp'),msg,()=>{$('#qnext').style.display='block';$('#qnext').textContent=(lives<=0||qi>=qs.length)?'HASIL':'LANJUT'},18)}
$('#qnext').onclick=()=>{if(!helperOpen)nextQ()};
function endQuiz(){const win=lives>0;A.sfx(win?'win':'bad');
 ov(win?'KUIS SELESAI!':'NYAWA HABIS',`Skor: ${qscore}<br>Nyawa tersisa: ${lives}`,[['MAIN LAGI',startQuiz],['MENU',()=>show('menu')]])}
/* ---------- TIMER ---------- */
setInterval(()=>{if(helperOpen||ovOpen)return;
 if(mode=='p'&&playing){time--;hud();if(time<=0){playing=false;clearSel();score=Math.max(0,score-50);A.sfx('bad');hud();ov('WAKTU HABIS','Reaksi gagal.<br>Skor -50',[['ULANGI',startLevel],['MENU',()=>show('menu')]])}}
 if(mode=='q'&&qLive){qt--;barUp();if(qt<=0)ans(null)}},1000);
/* ---------- KARAKTER EASTER EGG ---------- */
const SPR=['.4k8.4','.3k4s2k4.3','.1k6s2k6.1','.1k5s4k5.1','.1k3s8k3.1','.1k2s10k2.1','.1k1s1g10s1k1.1','.1k1s1g1w1p1g1s2g1p1w1g1s1k1.1',
'.1k1s1g4s2g4s1k1.1','.2s12.2','.2s5m4s3.2','.3S10.3','.5s6.5','.1W6x2W6.1','.1W6x2W6.1','.1W6x2W6.1','.1W14.1'];
const PAL={k:'#2a1a12',s:'#c68a57',S:'#a86d3f',g:'#1b1b2f',w:'#f4fdff',p:'#1b1b2f',m:'#7b2a2a',W:'#eafaff',x:'#ff2d95'};
(()=>{const x=$('#sprite').getContext('2d');SPR.forEach((rl,y)=>{let c=0;rl.replace(/(.)(\d+)/g,(m,ch,n)=>{for(let i=0;i<+n;i++){if(ch!='.'){x.fillStyle=PAL[ch];x.fillRect(c,y,1,1)}c++}})})})();
function sched(){clearTimeout(hT);hT=setTimeout(helper,40000+Math.random()*50000)}
function helper(){
 if(!mode||ovOpen||helperOpen||!((mode=='p'&&playing)||(mode=='q'&&qLive))){sched();return}
 helperOpen=true;dn=null;$('#lock').style.display='block';const h=$('#helper');h.className='c'+(Math.random()*4|0);h.style.display='flex';A.sfx('pop');
 $('#hb').style.display='none';
 tw($('#hq'),['Hmph. Lama banget. Mau aku bantu?','Kasihan deh... Mau aku bantu?','Gampang sebenernya. Mau aku bantu?'][Math.random()*3|0],()=>$('#hb').style.display='block')}
$('#b1').onclick=()=>{$('#hb').style.display='none';
 if(mode=='p'){time+=15;hud()}else{qt+=15;barUp()}A.sfx('zap');
 tw($('#hq'),'Nih +15 detik. Jangan bilang siapa-siapa.',()=>setTimeout(()=>{$('#helper').style.display='none';$('#lock').style.display='none';helperOpen=false;sched()},1200))};
/* ---------- MENU & INIT ---------- */
[['C','#ff2d95'],['H','#fff'],['C','#ff2d95'],['O','#ffe629'],['H','#19d3e6']].forEach(([l,c],i)=>{const d=document.createElement('i');d.textContent=l;d.style.background=c;d.style.color=c=='#ff2d95'?'#fff':'#1b1b2f';d.style.animationDelay=i*.15+'s';$('#deco').appendChild(d)});
$('#m1').onclick=()=>{show('puz');startLevel()};
$('#m2').onclick=()=>{show('quiz');startQuiz()};
$('#back1').onclick=$('#back2').onclick=()=>{if(!helperOpen&&!ovOpen)ov('KEMBALI KE MENU?','Progres mode ini akan hilang.',[['YA',()=>show('menu')],['BATAL',()=>{}]])};
addEventListener('resize',()=>{if(cd&&mode=='p')layout()});
show('menu');
</script></body></html>
"""

components.html(GAME_HTML, height=1000, scrolling=True)
