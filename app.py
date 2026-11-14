"""Isomer Match - puzzle isomer kimia retro pixel art.
Jalankan: streamlit run app.py
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Isomer Match", page_icon="🧪", layout="wide",
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
#app{max-width:480px;margin:0 auto;padding:8px}
.px{border:3px solid var(--ink);box-shadow:3px 3px 0 var(--ink);background:#fff}
h1{margin:0 0 8px;background:var(--pk);color:#fff;text-align:center;padding:10px 4px;font-size:15px;text-shadow:2px 2px 0 var(--ink)}
h1 small{display:block;color:var(--yl);font-size:7px;margin-top:6px}
#hud{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:8px}
#hud div{padding:5px 2px;text-align:center;font-size:7px;background:var(--yl)}
#hud b{display:block;font-size:11px;margin-top:4px}
#info{padding:8px;margin-bottom:8px;font-size:7px;line-height:1.7;display:flex;gap:10px;align-items:center;background:var(--cl)}
#mini{display:grid;gap:1px;flex:none;padding:3px;background:#fff;border:2px solid var(--ink)}
.m{width:9px;height:9px}.m.C{background:var(--pk)}.m.H{background:var(--cy)}.m.O{background:var(--yl);outline:1px solid var(--ink)}
#board{position:relative;margin:0 auto 8px;background:var(--cl)}
.cell{position:absolute;border:1px solid #92e6f0;font-size:8px;display:flex;align-items:center;justify-content:center}
.cell.Z{background:repeating-linear-gradient(45deg,#fff3a0 0 6px,#ffe629 6px 12px);color:#a06b00}
.cell.P{background:#fff;color:#079;box-shadow:inset 0 0 0 3px var(--cy)}
.cell.N{background:#ffd3ea;color:#c0156b;box-shadow:inset 0 0 0 3px var(--pk)}
.cell.I{background:#ff3b3b;color:#fff}
.t{position:absolute;display:flex;align-items:center;justify-content:center;font-size:13px;border:3px solid var(--ink);
transition:left .12s,top .12s;cursor:pointer;z-index:2;box-shadow:inset -3px -3px 0 rgba(0,0,0,.18)}
.t.C{background:var(--pk);color:#fff}.t.H{background:#fff;color:var(--ink)}.t.O{background:var(--yl)}
.t.sh{animation:sh .2s}@keyframes sh{25%{transform:translateX(-3px)}75%{transform:translateX(3px)}}
.fl{position:absolute;z-index:5;font-size:8px;pointer-events:none;animation:up .9s forwards;text-shadow:1px 1px 0 #fff;white-space:nowrap}
@keyframes up{to{transform:translateY(-26px);opacity:0}}
#ctl{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-bottom:8px}
button{font-family:inherit;font-size:7px;padding:9px 4px;background:var(--cy);color:var(--ink);border:3px solid var(--ink);box-shadow:3px 3px 0 var(--ink);cursor:pointer}
button:active{transform:translate(3px,3px);box-shadow:none}
#lg{padding:8px;font-size:6px;line-height:2;background:#fff}
#lg i{display:inline-block;width:14px;height:10px;border:2px solid var(--ink);vertical-align:middle;margin-right:4px;font-style:normal}
#ov{position:fixed;inset:0;background:rgba(25,211,230,.88);display:flex;align-items:center;justify-content:center;z-index:50;padding:14px}
#ov .box{max-width:380px;padding:16px;text-align:center;line-height:1.9;font-size:8px}
#ov h2{margin:0 0 10px;font-size:13px;color:var(--pk);text-shadow:2px 2px 0 var(--ink)}
#ov button{margin-top:12px;background:var(--yl);font-size:9px;padding:11px 14px}
#helper{position:fixed;z-index:60;display:none;gap:6px;align-items:flex-end;animation:pop .35s steps(5)}
@keyframes pop{from{transform:scale(.2);opacity:0}}
#helper.c0{top:6px;left:6px}#helper.c1{top:6px;right:6px;flex-direction:row-reverse}
#helper.c2{bottom:6px;left:6px}#helper.c3{bottom:6px;right:6px;flex-direction:row-reverse}
#sprite{width:80px;height:85px;image-rendering:pixelated;flex:none;
filter:drop-shadow(1px 0 0 #1b1b2f) drop-shadow(-1px 0 0 #1b1b2f) drop-shadow(0 1px 0 #1b1b2f) drop-shadow(0 -1px 0 #1b1b2f)}
.bub{width:172px;padding:8px;font-size:7px;line-height:1.7;background:#fff}
#hb{display:flex;flex-direction:column;gap:5px;margin-top:6px}
#hb button{padding:6px 3px;font-size:6px;background:var(--yl)}#hb button:last-child{background:#fff}
</style></head><body>
<div id="app">
 <h1>ISOMER MATCH<small>LAB PIXEL PUZZLE</small></h1>
 <div id="hud"><div class="px">LEVEL<b id="lv">1</b></div><div class="px">SKOR<b id="sc">0</b></div><div class="px">WAKTU<b id="tm">0</b></div><div class="px">LANGKAH<b id="mv">0</b></div></div>
 <div id="info" class="px"></div>
 <div id="board" class="px"></div>
 <div id="ctl"><button id="rs">ULANG</button><button id="mu">MUSIK: ON</button><button id="tr">LAGU: CHIP LAB</button></div>
 <div id="lg" class="px"><i style="background:#fff;box-shadow:inset 0 0 0 2px #19d3e6"></i>Pt / <i style="background:#ffd3ea;box-shadow:inset 0 0 0 2px #ff2d95"></i>Ni katalis: balok meluncur instan<br>
 <i style="background:#ff3b3b"></i>Inhibitor: -3 detik, -15 poin<br><i style="background:#ffe629"></i>Zona reaktif x2: bonus skor</div>
</div>
<div id="ov"><div class="box px"><h2 id="ovt"></h2><div id="ovb"></div><button id="ovbtn"></button></div></div>
<div id="helper"><canvas id="sprite" width="16" height="17"></canvas>
 <div class="bub px"><div id="hq"></div><div id="hb"><button id="b1">+10 DETIK</button><button id="b2">AUTO-SOLVE</button><button id="b3">GAK USAH</button></div></div></div>
<script>
const $=s=>document.querySelector(s),COLS=8,ROWS=6;
/* ---------- DATA LEVEL ---------- */
const B=[
['Alkana','C4H10',['Butana',['.HHHH.','HCCCCH','.HHHH.']],['Isobutana',['..HHH..','..HCH..','.HCCCH.','..HHH..']]],
['Alkena','C4H8',['1-Butena',['.HHHH.','HCCCCH','...HH.']],['2-Butena',['.HH.H.','HCCCCH','.H.HH.']]],
['Alkohol (-OH)','C3H8O',['1-Propanol',['.HHH..','HCCCOH','.HHH..']],['2-Propanol',['..H..','.HOH.','HCCCH','.HHH.']]],
['Asam karboksilat (-COOH)','C4H8O2',['Asam butanoat',['.HHHO..','HCCCCOH','.HHH...']],['Asam 2-metilpropanoat',['..HHH..','..HCO..','.HCCCOH','..HH...']]]
].map(l=>({type:l[0],f:l[1],a:{name:l[2][0],rows:l[2][1]},b:{name:l[3][0],rows:l[3][1]}}));
const LV=B.concat(B.map(l=>({...l,a:l.b,b:l.a})));
/* ---------- AUDIO (WebAudio 8-bit) ---------- */
const A={c:null,on:false,tr:0,st:0,nt:0,id:0,
init(){if(this.c)return;this.c=new(window.AudioContext||window.webkitAudioContext)();this.m=this.c.createGain();this.m.gain.value=.25;this.m.connect(this.c.destination);
 const n=this.c.createBuffer(1,4410,44100),d=n.getChannelData(0);for(let i=0;i<4410;i++)d[i]=Math.random()*2-1;this.nb=n},
f:m=>440*2**((m-69)/12),
t(m,t,d,ty='square',v=.3){const c=this.c,o=c.createOscillator(),g=c.createGain();o.type=ty;o.frequency.value=this.f(m);
 g.gain.setValueAtTime(v,t);g.gain.exponentialRampToValueAtTime(.001,t+d);o.connect(g);g.connect(this.m);o.start(t);o.stop(t+d+.02)},
n(t,v=.1){const c=this.c,s=c.createBufferSource(),g=c.createGain();s.buffer=this.nb;g.gain.setValueAtTime(v,t);g.gain.exponentialRampToValueAtTime(.001,t+.05);s.connect(g);g.connect(this.m);s.start(t)},
TR:[
{name:'CHIP LAB',bpm:150,step(i,t,d){const M=[72,0,76,0,79,76,72,0,74,0,77,0,81,77,74,0,71,0,74,0,79,74,71,0,72,76,79,84,79,76,72,0],R=[48,50,43,48],k=i%32;
 if(M[k])this.t(M[k],t,d*.9,'square',.18);if(k%2==0)this.t(R[k>>3]+(k%8==4?12:0),t,d*.8,'triangle',.35);if(k%2)this.n(t)}},
{name:'DREAMY POP',bpm:92,step(i,t,d){const C=[[53,57,60,64],[55,59,62,67],[52,55,59,62],[57,60,64,67]],
 M=[76,0,0,74,72,0,0,0,74,0,0,71,67,0,0,0,71,0,0,74,76,0,0,0,72,0,0,69,0,0,0,0],k=i%32,ch=C[k>>3],p=[0,1,2,3,2,1,2,3][k%8];
 this.t(ch[p]+12,t,d*1.6,'triangle',.22);if(k%8==0){ch.forEach(x=>this.t(x,t,d*7,'sine',.1));this.t(ch[0]-12,t,d*7,'triangle',.3)}
 if(M[k])this.t(M[k],t,d*3,'square',.1);if(k%4==2)this.n(t,.05)}}],
tick(){const T=this.TR[this.tr],d=60/T.bpm/2;while(this.nt<this.c.currentTime+.25){T.step.call(this,this.st,this.nt,d);this.nt+=d;this.st++}},
play(){this.init();this.c.resume();this.on=true;this.nt=this.c.currentTime+.05;this.st=0;clearInterval(this.id);this.id=setInterval(()=>this.tick(),60)},
stop(){this.on=false;clearInterval(this.id)},
sfx(k){if(!this.c)return;const t=this.c.currentTime,s=(a,ty,v,d=.08)=>a.forEach((m,i)=>this.t(m,t+i*.06,d,ty,v));
 ({mv:()=>s([79],'square',.2,.06),bump:()=>s([40],'sawtooth',.2,.1),zap:()=>s([84,88,91],'square',.2),bad:()=>s([40,36],'sawtooth',.3,.25),
 win:()=>s([72,76,79,84,88,91],'square',.25,.15),pop:()=>s([88,95],'square',.15,.12)})[k]()}};
/* ---------- STATE ---------- */
let lv=0,score=0,time=0,moves=0,playing=false,helperOpen=false,ovOpen=true,grid,sp,cd,tiles,used,tg,cell,drag=null,hT,hc;
const board=$('#board'),fm=s=>s.replace(/(\d+)/g,'<sub>$1</sub>');
const sig=a=>{const m=[];a.forEach((r,i)=>r.forEach((x,j)=>x&&x!='.'&&m.push([i,j,x])));
 const r0=Math.min(...m.map(x=>x[0])),c0=Math.min(...m.map(x=>x[1]));return m.map(x=>(x[0]-r0)+','+(x[1]-c0)+x[2]).sort().join('|')};
const free=(r,c)=>r>=0&&c>=0&&r<ROWS&&c<COLS&&!grid[r][c];
const hud=()=>{$('#lv').textContent=(lv+1)+'/'+LV.length;$('#sc').textContent=score;$('#tm').textContent=time;$('#mv').textContent=moves};
function cs(){return Math.min(52,Math.floor((Math.min(innerWidth,480)-28)/COLS))}
function place(t){t.el.style.left=t.c*cell+2+'px';t.el.style.top=t.r*cell+2+'px'}
function layout(){cell=cs();board.style.width=COLS*cell+6+'px';board.style.height=ROWS*cell+6+'px';
 cd.forEach((row,r)=>row.forEach((e,c)=>Object.assign(e.style,{left:c*cell+'px',top:r*cell+'px',width:cell+'px',height:cell+'px'})));
 tiles.forEach(t=>{t.el.style.width=t.el.style.height=cell-4+'px';place(t)})}
function ov(t,h,b,fn){$('#ovt').innerHTML=t;$('#ovb').innerHTML=h;$('#ovbtn').textContent=b;$('#ov').style.display='flex';ovOpen=true;
 $('#ovbtn').onclick=()=>{$('#ov').style.display='none';ovOpen=false;fn()}}
function fl(txt,r,c,col){const d=document.createElement('div');d.className='fl';d.textContent=txt;d.style.cssText+=`left:${c*cell}px;top:${r*cell}px;color:${col}`;board.appendChild(d);setTimeout(()=>d.remove(),900)}
/* ---------- LEVEL ---------- */
function startLevel(){
 const L=LV[lv],rows=L.a.rows,h=rows.length,w=rows[0].length,or=(ROWS-h)>>1,oc=(COLS-w)>>1;
 board.innerHTML='';grid=[...Array(ROWS)].map(()=>Array(COLS).fill(null));sp=[...Array(ROWS)].map(()=>Array(COLS).fill(''));
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
 tr.forEach(s=>[...s].forEach(ch=>{const d=document.createElement('div');d.className='m '+ch;mi.appendChild(d)}));
 hud();sched()}
/* ---------- GERAK ---------- */
function move(t,dr,dc){
 if(!playing||helperOpen)return;
 if(!free(t.r+dr,t.c+dc)){A.sfx('bump');t.el.classList.add('sh');setTimeout(()=>t.el.classList.remove('sh'),200);return}
 moves++;let slide=false;
 while(free(t.r+dr,t.c+dc)){
  grid[t.r][t.c]=null;t.r+=dr;t.c+=dc;grid[t.r][t.c]=t;
  const k=sp[t.r][t.c],key=t.r+','+t.c;
  if(k=='I'){score=Math.max(0,score-15);time=Math.max(1,time-3);fl('-3s -15',t.r,t.c,'#e00');A.sfx('bad');break}
  if(k=='Z'&&!used.has(key)){used.add(key);score+=20;fl('x2 +20',t.r,t.c,'#c80');A.sfx('zap')}
  if(k=='P'||k=='N'){slide=true;if(!used.has(key)){used.add(key);score+=25;fl((k=='P'?'Pt':'Ni')+'! +25',t.r,t.c,'#079');A.sfx('zap')}}
  if(!slide)break}
 place(t);if(!slide)A.sfx('mv');hud();
 if(sig(grid.map(row=>row.map(x=>x&&x.type)))==tg)setTimeout(()=>done(false),250)}
board.onpointerdown=e=>{const el=e.target.closest('.t');if(el)drag={t:tiles.find(t=>t.el===el),x:e.clientX,y:e.clientY}};
window.onpointerup=e=>{if(!drag)return;const{t,x,y}=drag;drag=null;const dx=e.clientX-x,dy=e.clientY-y;let d;
 if(Math.hypot(dx,dy)>14)d=Math.abs(dx)>Math.abs(dy)?[0,Math.sign(dx)]:[Math.sign(dy),0];
 else{const o=[[0,1],[1,0],[0,-1],[-1,0]].filter(a=>free(t.r+a[0],t.c+a[1]));
  if(!o.length){move(t,0,1);return}
  const rc=t.el.getBoundingClientRect(),tx=e.clientX-rc.left-rc.width/2,ty=e.clientY-rc.top-rc.height/2;
  o.sort((p,q)=>(q[1]*tx+q[0]*ty)-(p[1]*tx+p[0]*ty));d=o[0]}
 move(t,d[0],d[1])};
function done(auto){if(!playing)return;playing=false;const b=auto?100:200+time*5+Math.max(0,150-moves*3),last=lv==LV.length-1;score+=b;hud();A.sfx('win');
 ov(last?'SEMUA ISOMER BERHASIL!':'ISOMER MATCH!',`${LV[lv].b.name} terbentuk${auto?' (dibantu)':''}.<br>Bonus +${b}<br>Skor: ${score}`,last?'MAIN LAGI':'LEVEL BERIKUT',()=>{if(last){lv=0;score=0}else lv++;startLevel()})}
function autoSolve(){const L=LV[lv],rows=L.b.rows,or=(ROWS-rows.length)>>1,oc=(COLS-rows[0].length)>>1,left=[...tiles];
 grid.forEach(r=>r.fill(null));
 rows.forEach((s,r)=>[...s].forEach((ch,c)=>{if(ch=='.')return;let bi=-1,bd=1e9;
  left.forEach((t,i)=>{if(t.type==ch){const d=Math.abs(t.r-r-or)+Math.abs(t.c-c-oc);if(d<bd){bd=d;bi=i}}});
  const t=left.splice(bi,1)[0];t.r=r+or;t.c=c+oc;grid[t.r][t.c]=t;place(t)}));
 setTimeout(()=>done(true),400)}
/* ---------- TIMER ---------- */
setInterval(()=>{if(!playing||helperOpen)return;time--;hud();
 if(time<=0){playing=false;score=Math.max(0,score-50);A.sfx('bad');hud();ov('WAKTU HABIS','Reaksi gagal.<br>Skor -50','ULANGI',startLevel)}},1000);
/* ---------- KARAKTER EASTER EGG ---------- */
const SPR=['.4k8.4','.3k4s2k4.3','.1k6s2k6.1','.1k5s4k5.1','.1k3s8k3.1','.1k2s10k2.1','.1k1s1g10s1k1.1','.1k1s1g1w1p1g1s2g1p1w1g1s1k1.1',
'.1k1s1g4s2g4s1k1.1','.2s12.2','.2s5m4s3.2','.3S10.3','.5s6.5','.1W6x2W6.1','.1W6x2W6.1','.1W6x2W6.1','.1W14.1'];
const PAL={k:'#2a1a12',s:'#c68a57',S:'#a86d3f',g:'#1b1b2f',w:'#f4fdff',p:'#1b1b2f',m:'#7b2a2a',W:'#eafaff',x:'#ff2d95'};
(()=>{const x=$('#sprite').getContext('2d');SPR.forEach((rl,y)=>{let c=0;rl.replace(/(.)(\d+)/g,(m,ch,n)=>{for(let i=0;i<+n;i++){if(ch!='.'){x.fillStyle=PAL[ch];x.fillRect(c,y,1,1)}c++}})})})();
function sched(){clearTimeout(hT);hT=setTimeout(helper,15000+Math.random()*25000)}
function helper(){if(!playing||helperOpen||ovOpen){sched();return}
 helperOpen=true;const h=$('#helper');h.className='c'+(Math.random()*4|0);h.style.display='flex';A.sfx('pop');
 $('#hq').textContent=['Hmph. Lama banget. Mau aku bantu?','Kasihan deh... Mau aku bantu?','Gampang sebenernya. Mau aku bantu?'][Math.random()*3|0];
 $('#hb').style.display='flex';clearTimeout(hc);hc=setTimeout(()=>say('Yaudah, gengsi itu penting.'),14000)}
function say(txt,act){$('#hq').textContent=txt;$('#hb').style.display='none';clearTimeout(hc);if(act)act();
 setTimeout(()=>{$('#helper').style.display='none';helperOpen=false;sched()},1800)}
$('#b1').onclick=()=>say('Nih +10 detik. Jangan bilang siapa-siapa.',()=>{time+=10;hud();A.sfx('zap')});
$('#b2').onclick=()=>say('Gampang. Duduk manis aja, ya.',autoSolve);
$('#b3').onclick=()=>say('Sombong amat. Ya udah.');
/* ---------- KONTROL ---------- */
$('#rs').onclick=()=>{if(!ovOpen&&!helperOpen)startLevel()};
$('#mu').onclick=()=>{if(A.on)A.stop();else A.play();$('#mu').textContent='MUSIK: '+(A.on?'ON':'OFF')};
$('#tr').onclick=()=>{A.tr=(A.tr+1)%A.TR.length;$('#tr').textContent='LAGU: '+A.TR[A.tr].name;if(A.on)A.play()};
addEventListener('resize',()=>{if(cd)layout()});
ov('ISOMER MATCH','Ubah susunan atom (C, H, O) menjadi <b>isomer target</b>.<br>Tap / swipe balok ke ruang kosong.<br>Pt/Ni: meluncur instan. Merah: hati-hati. Zona kuning: bonus x2.<br>Waktu habis = reaksi gagal.','MULAI',()=>{A.play();startLevel()});
</script></body></html>
"""

components.html(GAME_HTML, height=980, scrolling=True)
