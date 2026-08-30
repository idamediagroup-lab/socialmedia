const pptxgen=require('pptxgenjs');
const fs=require('fs');
const p=new pptxgen();
p.layout='LAYOUT_WIDE';           // 13.333 x 7.5
p.author='Get AI Leads Now'; p.title='The Score Machine — Masterclass';
const LIGHT='bg_light.jpg', DARK='bg_dark.jpg';
const RED='D61A20', GRN='2ECC34', GOLD='D6A83A', INK='0A0A0C', SLATE='2A2E33', MUTE='6B7280', W='FFFFFF';
const HF='Arial', BF='Calibri';
const X=0.85, CW=11.6;            // content zone
let N=0; const notes=[];

p.defineSlideMaster({title:'LIGHT',background:{path:LIGHT}});
p.defineSlideMaster({title:'DARK',background:{path:DARK}});

/* auto-fit: shrink font until the longest line fits the box width */
function fit(text,boxW,maxSize,bold){
  const em=bold?0.60:0.52;                 // Arial avg advance width
  const lines=String(text).split('\n');
  const longest=Math.max(...lines.map(l=>l.length));
  const cap=Math.floor((boxW*72*0.97)/(longest*em));
  return Math.max(14,Math.min(maxSize,cap));
}
function S(dark){const s=p.addSlide({masterName:dark?'DARK':'LIGHT'});N++;return s;}
function note(s,t){if(t)s.addNotes(t);}
function dots(s,x,y){const c=[RED,GOLD,GRN];c.forEach((k,i)=>s.addShape(p.ShapeType.ellipse,{x:x+i*0.28,y,w:0.17,h:0.17,fill:{color:k}}));}
function kicker(s,t,dark){s.addText(t,{x:X,y:0.72,w:CW,h:0.34,isTextBox:true,margin:0,fontFace:HF,fontSize:13,bold:true,charSpacing:3,color:dark?GOLD:MUTE});}
function H(s,t,o={}){s.addText(t,{x:X,y:o.y??1.25,w:o.w??CW,h:o.h??1.9,isTextBox:true,margin:0,fontFace:HF,fontSize:fit(t,o.w??CW,o.size??46,true),bold:true,color:o.color??(o.dark?W:INK),align:o.align??'left',lineSpacing:o.ls??52});}

/* ---------- slide types ---------- */
function title(t,sub,nt){const s=S(true);dots(s,X,1.35);
 s.addText(t,{x:X,y:1.8,w:CW,h:2.2,isTextBox:true,margin:0,fontFace:HF,fontSize:fit(t,CW,72,true),bold:true,color:W,lineSpacing:80});
 s.addText(sub,{x:X,y:4.1,w:CW,h:0.9,isTextBox:true,margin:0,fontFace:BF,fontSize:24,color:'D8DCE1'});note(s,nt);return s;}

function statement(t,sub,o={}){const s=S(o.dark);dots(s,X,1.15);
 s.addText(t,{x:X,y:1.6,w:CW,h:2.7,isTextBox:true,margin:0,fontFace:HF,fontSize:fit(t,CW,o.size??58,true),bold:true,color:o.dark?W:INK,lineSpacing:o.ls??64});
 if(sub)s.addText(sub,{x:X,y:4.5,w:CW,h:1.1,isTextBox:true,margin:0,fontFace:BF,fontSize:26,color:o.dark?'C9CFD6':SLATE});
 note(s,o.n);return s;}

function ask(q,why){const s=S(true);
 s.addShape(p.ShapeType.roundRect,{x:X,y:1.0,w:3.5,h:0.75,rectRadius:0.12,fill:{color:GRN}});
 s.addText('TYPE IN THE CHAT',{x:X,y:1.0,w:3.5,h:0.75,isTextBox:true,margin:0,fontFace:HF,fontSize:19,bold:true,color:INK,align:'center',valign:'middle'});
 s.addText(q,{x:X,y:2.25,w:CW,h:3.0,isTextBox:true,margin:0,fontFace:HF,fontSize:fit(q,CW,46,true),bold:true,color:W,lineSpacing:56});
 note(s,why);return s;}

function pain(t,lines,nt){const s=S();dots(s,X,1.0);
 H(s,t,{y:1.45,size:44,h:1.2});
 let y=3.0;lines.forEach(l=>{s.addText(l,{x:X,y,w:CW,h:0.62,isTextBox:true,margin:0,fontFace:BF,fontSize:30,color:SLATE});y+=0.68;});
 note(s,nt);return s;}

function bullets(t,items,o={}){const s=S(o.dark);dots(s,X,0.95);
 H(s,t,{y:1.35,size:o.hsize??40,h:1.0,dark:o.dark});
 const top=2.55, BOT=6.62, gap=0.14, n=items.length;
 let bh=Math.min(o.bh??0.85,(BOT-top-gap*(n-1))/n);
 let fs=o.fs??(bh>=0.75?21:bh>=0.62?19:17);
 let y=top;
 items.forEach((it,i)=>{
   s.addShape(p.ShapeType.roundRect,{x:X,y,w:CW,h:bh,rectRadius:0.1,fill:{color:o.dark?'16181C':'FFFFFF'},line:{color:o.dark?'2C3238':'DFE3E7',width:1}});
   const d=Math.min(0.44,bh-0.16);
   if(o.num){s.addShape(p.ShapeType.ellipse,{x:X+0.24,y:y+(bh-d)/2,w:d,h:d,fill:{color:o.tone??INK}});
     s.addText(String(i+1),{x:X+0.24,y:y+(bh-d)/2,w:d,h:d,isTextBox:true,margin:0,fontFace:HF,fontSize:Math.round(d*38),bold:true,color:W,align:'center',valign:'middle'});}
   s.addText(it,{x:X+(o.num?0.92:0.42),y,w:CW-(o.num?1.3:0.8),h:bh,isTextBox:true,margin:0,fontFace:BF,fontSize:fs,color:o.dark?'E6EAEE':SLATE,valign:'middle'});
   y+=bh+gap;});
 note(s,o.n);return s;}

function stat(big,label,sub,o={}){const s=S(true);dots(s,X,1.1);
 s.addText(big,{x:X,y:1.7,w:CW,h:2.4,isTextBox:true,margin:0,fontFace:HF,fontSize:fit(big,CW,o.size??150,true),bold:true,color:o.color??RED});
 s.addText(label,{x:X,y:4.15,w:CW,h:0.7,isTextBox:true,margin:0,fontFace:HF,fontSize:30,bold:true,color:W});
 if(sub)s.addText(sub,{x:X,y:4.95,w:CW,h:0.8,isTextBox:true,margin:0,fontFace:BF,fontSize:21,color:'AEB6BF'});
 note(s,o.n);return s;}

function blueprint(marks,t,nt){const s=S();dots(s,X,0.85);
 H(s,t,{y:1.2,size:34,h:0.7});
 const L=['700 credit score?','Under 30% utilization?','5 open primary cards, 2 yrs good history?','3 primary cards, 3 yrs old, $5,000 limit?','More than 4 unsecured accounts in 12 months?','Under 4 inquiries?','Collections?','Charge-offs?','Late payments?','Bankruptcy?'];
 const col={R:RED,Y:GOLD,G:GRN,N:'C7CDD4'};
 let y=2.15,x=X,i=0;
 L.forEach((l,k)=>{
   if(k===5){y=2.15;x=X+CW/2+0.15;}
   const cw=CW/2-0.15;
   s.addShape(p.ShapeType.roundRect,{x,y,w:cw,h:0.62,rectRadius:0.08,fill:{color:'FFFFFF'},line:{color:'DFE3E7',width:1}});
   s.addShape(p.ShapeType.ellipse,{x:x+0.16,y:y+0.19,w:0.24,h:0.24,fill:{color:col[marks?marks[k]:'N']}});
   s.addText(`${k+1}. ${l}`,{x:x+0.52,y,w:cw-0.68,h:0.62,isTextBox:true,margin:0,fontFace:BF,fontSize:14,color:SLATE,valign:'middle'});
   y+=0.72;});
 note(s,nt);return s;}

function compare(t,aT,aRows,bT,bRows,nt){const s=S();dots(s,X,0.9);
 H(s,t,{y:1.25,size:40,h:0.9});
 const cw=CW/2-0.2;
 [[X,aT,aRows,RED],[X+CW/2+0.2,bT,bRows,GRN]].forEach(([x,head,rows,c])=>{
   s.addShape(p.ShapeType.roundRect,{x,y:2.5,w:cw,h:3.55,rectRadius:0.12,fill:{color:'FFFFFF'},line:{color:'DFE3E7',width:1}});
   s.addShape(p.ShapeType.roundRect,{x:x+0.3,y:2.75,w:1.5,h:0.45,rectRadius:0.08,fill:{color:c}});
   s.addText(head,{x:x+0.3,y:2.75,w:1.5,h:0.45,isTextBox:true,margin:0,fontFace:HF,fontSize:14,bold:true,color:W,align:'center',valign:'middle'});
   let y=3.45;rows.forEach(r=>{s.addText(r,{x:x+0.3,y,w:cw-0.6,h:0.5,isTextBox:true,margin:0,fontFace:BF,fontSize:20,color:SLATE});y+=0.55;});});
 note(s,nt);return s;}

function price(strike,now,sub,o={}){const s=S(true);dots(s,X,1.0);
 let y=1.6;
 if(strike){s.addText(strike,{x:X,y,w:CW,h:1.0,isTextBox:true,margin:0,fontFace:HF,fontSize:64,bold:true,color:'6B7280',strike:true});y+=1.15;}
 s.addText(now,{x:X,y,w:CW,h:1.9,isTextBox:true,margin:0,fontFace:HF,fontSize:fit(now,CW,o.size??120,true),bold:true,color:o.color??W});
 if(sub)s.addText(sub,{x:X,y:y+2.0,w:CW,h:0.7,isTextBox:true,margin:0,fontFace:BF,fontSize:o.subSize??26,color:'C9CFD6'});
 note(s,o.n);return s;}

function divider(t,sub,nt){const s=S(true);dots(s,X,2.3);
 s.addText(t,{x:X,y:2.75,w:CW,h:1.6,isTextBox:true,margin:0,fontFace:HF,fontSize:fit(t,CW,60,true),bold:true,color:W});
 if(sub)s.addText(sub,{x:X,y:4.4,w:CW,h:0.8,isTextBox:true,margin:0,fontFace:BF,fontSize:24,color:'AEB6BF'});
 note(s,nt);return s;}
module.exports={};

/* ================= ACT 1 ================= */
title('THE SCORE MACHINE','Why you got denied — and what to do about it','Ninety minutes. By the end you will know exactly why your last denial happened, and what your file needs before you apply to anything again.');
ask('Type YES if you can see my screen\nand hear me clearly.','ASK #1. Must be trivially easy and must succeed — it teaches the room that typing in the chat is what we do here. If the chat stays quiet, stop and fix it. Every later ask depends on this one landing.');
statement('You didn\'t get turned down\nfor the reason you think.','',{dark:true,size:56,n:'Say nothing. Three full seconds of silence. Let it sit before you move.'});
pain('THE HOUSE',['You found the house.','You got pre-approved.','Then you weren\'t.'],'Some of you know exactly what that phone call sounds like.');
pain('THE CAR',['You need the car to get to work.','The job is what feeds your family.','The denial costs you both.'],'SLOW DOWN. This is the slide people feel. Nobody applies for a car loan because they want a car loan — they want to stop losing shifts and get home before their kids are asleep. Do not rush this slide.');
ask('Type YES if a denial has ever cost you\nsomething that mattered more\nthan the money.','ASK #2 — first emotional yes. Wait for it. Read two or three names out loud; that is what teaches the room that answering gets acknowledged.');
pain('THE CONTRACT',['The contract was yours.','You didn\'t have the capital to staff it.','So you watched someone else take it.'],'For the business owners — same feeling, different shape. You weren\'t short on skill. You were short on cash for ninety days.');
statement('NOBODY WANTS\nA CREDIT SCORE.','They want what it unlocks.',{size:62,n:'Nobody has ever laid in bed wishing their score was higher for its own sake. You want the house. You want the truck. You want the line of credit. The score is just the door.'});
statement('This isn\'t a class about credit.\nIt\'s a class about approvals.','',{size:48});
bullets('LET\'S SEE IF I\'M DESCRIBING YOUR SITUATION',['Denied — and the letter never really told you why','Your score is "fine." 640. 700. Still denied.','Solid card, still stuck at a $500 limit, calling it progress','You have cards. You still aren\'t fundable.'],{n:'Read all four slowly. Then go straight to the ask.'});
ask('Type YES if even one\nof those four is you.','ASK #3 — highest-volume yes of the night. Wait. Do not move until the chat fills. The wall of YES is the point, not the answer: it proves to every person that they are not the only one.');
bullets('BOTH ROOMS. ONE MACHINE.',['Some of you are here for personal credit','Some of you are here for business funding','Same file. Same rules. Same machine.'],{n:'Nobody is in the wrong room tonight. Underwriting does not read a file differently because of what you want at the end of it.'});
ask('Type 1 for personal credit.\nType 2 for business funding.\nType 3 if it\'s both.','ASK #4 — diagnostic, not agreement. Tells you the room mix so you can weight examples for the next hour. Say the split out loud once you see it.');
pain('WHO I AM',['[Your name] — Owner, Get AI Leads Now','I\'m not a credit repair company.','I\'m a business owner who uses this software.'],'LANGUAGE DISCIPLINE ALL NIGHT: always "they" and "Score Machine." Never "we," "our software," "our team." You are a customer telling the room what the product did for you. One slip into "we" costs the position.');
bullets('THE THREE WAYS I MAKE MONEY WITH IT',['On my own file — I know where I stand before I ever apply','For my clients — I help them get funded, and I charge for that','By referring it — I earn when you use my link. Tonight included.'],{num:true,fs:19,n:'DISCLOSURE SLIDE. Say it plainly: I get paid when someone signs up through my link, including anybody tonight. Delivering it yourself, early, converts a liability into proof — number three is a business model available to every person on this call. If asked directly in Q&A whether you work with Score Machine: answer honestly and briefly. Never deny a relationship you have.'});
pain('WHAT CHANGED IN MY BUSINESS',['Before: a client asked about funding — I had nothing.','Now: I read their file in minutes.','New service. Same clients.'],'FILL WITH YOUR OWN TRUE SPECIFICS. No revenue figure on this slide — a dollar amount is an earnings claim. End pointed at them: "and that is the last I will say about me."');
compare('LET ME BE STRAIGHT WITH YOU','WHAT THIS IS',['How underwriting reads your file','Software that does it in a minute','Where you actually stand tonight'],'WHAT IT ISN\'T',['A promise of an approval','A promise of a number','A miracle'],'I am not going to guarantee you an approval or tell you your score is going up 100 points. Nobody honest can. What I can do is show you the ten questions every lender asks about your file — and then show you your own answers.');
bullets('THE CHAIN',['You got denied','Because inquiries quietly lowered your ceiling','Because you applied without knowing if you were eligible','Eligibility can be known BEFORE you apply','If you\'re not eligible — the file gets fixed','Once you are — the bank and the bureau decide where you apply'],{num:true,bh:0.62,fs:19,n:'That is the whole ninety minutes on one slide. Tell them to screenshot it. Everything from here just fills it in.'});

/* ================= ACT 2 ================= */
statement('A score is not\nan approval.','',{dark:true,size:64,n:'A score gets you considered. It does not get you approved. Two different events, and nobody is taught the difference.'});
bullets('YOU DON\'T HAVE A CREDIT SCORE. YOU HAVE THREE FILES.',['EXPERIAN — its own data, its own score','EQUIFAX — its own data, its own score','TRANSUNION — its own data, its own score'],{num:true,n:'Different data. Different scores. Most people have three files and assume they have one.'});
statement('Which one\ndid they pull?','',{dark:true,size:66,n:'Think about your last denial. Right now. Which bureau did that lender pull? Pause. Let it be uncomfortable.'});
ask('Type YES if you have no idea\nwhich bureau your last\ndenial pulled.','ASK #5 — near-universal, and it is an admission rather than an agreement, which is stronger. Once they have typed it they have told themselves they have a gap. Follow with: "That is not your fault. Nobody ever told you it mattered."');
statement('Your best file doesn\'t\nget you approved.','The one they pulled does.',{size:52});
bullets('CREDIT DECAY',['Every application leaves an inquiry','Every inquiry lowers what a bank will extend you','It happens quietly — whether you were approved or not'],{num:true,n:'This is the part nobody tells you. It is not just a few points off a score. Inquiries lower the dollar amount a bank is willing to hand you.'});
ask('Type YES if nobody has ever\nexplained credit decay to you\nbefore tonight.','ASK #6 — establishes you as the one who told them. This is the authority beat of Act 2.');
stat('−$5,000','APPROVAL ODDS ON A REAL FILE','14 inquiries. The score never said a word about it.',{n:'Negative five thousand. This person is not getting a smaller approval — they are getting nothing, from anyone. And they would have kept applying.'});
statement('Forget about points.\nIt\'s about money.','',{dark:true,size:64});
bullets('SO WHAT ACTUALLY HAPPENED',['You applied','You didn\'t know if you qualified','You got denied','And the inquiry made the next one harder'],{num:true,bh:0.7});
statement('Denied → inquiry → lower ceiling\nDenied → inquiry → lower ceiling\nDenied.','',{size:40,ls:56,n:'This is why it feels like it is getting worse even though you are trying harder. You ARE trying harder. Every attempt is costing you the next one.'});
ask('Type YES if that\'s\nbeen your experience.','ASK #7 — they are now agreeing to your diagnosis of their own history. Everything after this is built on that yes.');
statement('There is a way\nto know first.','',{dark:true,size:66});

/* ================= ACT 3 ================= */
statement('The question is never\n"what\'s my score?"','The question is "should I apply at all?"',{size:48});
bullets('HOW IT STARTS',['Upload your credit report','No forms. No typing.','Five AIs read every line of it'],{num:true,n:'The file does the data entry. You do not type a name, an address, or an account number.'});
divider('THE UNDERWRITING BLUEPRINT','Ten questions. Every lender asks them.\nAlmost nobody has ever seen them written down.');
(function(){const s=S();dots(s,X,0.95);H(s,'RED. YELLOW. GREEN.',{y:1.35,size:44,h:1.0});
 const rows=[[RED,'RED','STOP'],[GOLD,'YELLOW','PROCEED WITH CAUTION'],[GRN,'GREEN','GO']];let y=2.75;
 rows.forEach(([c,a,b])=>{s.addShape(p.ShapeType.roundRect,{x:X,y,w:CW,h:0.95,rectRadius:0.1,fill:{color:'FFFFFF'},line:{color:'DFE3E7',width:1}});
  s.addShape(p.ShapeType.ellipse,{x:X+0.3,y:y+0.24,w:0.47,h:0.47,fill:{color:c}});
  s.addText(a,{x:X+1.0,y,w:2.2,h:0.95,isTextBox:true,margin:0,fontFace:HF,fontSize:24,bold:true,color:INK,valign:'middle'});
  s.addText(b,{x:X+3.2,y,w:CW-3.5,h:0.95,isTextBox:true,margin:0,fontFace:BF,fontSize:22,color:SLATE,valign:'middle'});y+=1.1;});
 note(s,'Like a traffic light. If you can drive a car, you can read a credit file. That is genuinely the whole skill.');})();
ask('Type YES if you can\nread a traffic light.','ASK #8 — deliberately easy and a little funny. Resets the energy after eight heavy minutes and plants the belief that this is learnable, right before you show them the ten lines.');
blueprint(null,'THE TEN QUESTIONS EVERY LENDER ASKS','Ten. That is what stands between you and every approval you have been denied. NOTE: line 5 direction must be locked before stage.');
ask('Type YES if you\'ve never seen\nthese ten questions written\ndown anywhere before.','ASK #9 — the value moment. They just received something they did not have. Get them to say so out loud.');
statement('Are you eligible?','',{dark:true,size:78});
statement('Let\'s read a real file.','You call it. Red, yellow, or green.',{size:52,n:'I read the line, you tell me. Do not be shy — you already know how to do this, you just have not been allowed to before.'});
blueprint(['R','R','G','Y','R','R','G','R','R','G'],'A REAL FILE — YOU CALL IT','LONGEST SLIDE IN THE DECK. Walk it one line at a time. Let the room answer each one out loud. DO NOT answer for them. (Marks shown are an example — replace with your actual demo file.)');
statement('Not eligible.\nAnd now you know exactly why.','Not "your credit is bad." Four specific lines.',{size:48,n:'That is the difference between how they felt walking in and how they feel now. "Bad credit" is a feeling. Four red lines is a to-do list.'});
(function(){const s=S(true);dots(s,X,0.95);H(s,'WHAT GREEN LOOKS LIKE',{y:1.35,size:42,h:0.9,dark:true});
 const cards=[['1','INQUIRY'],['0','COLLECTIONS'],['2%','UTILIZATION'],['10/10','GREEN LINES']];
 let x=X;cards.forEach(([n,l])=>{s.addShape(p.ShapeType.roundRect,{x,y:2.9,w:2.72,h:2.0,rectRadius:0.12,fill:{color:'16181C'},line:{color:GRN,width:2}});
  s.addText(n,{x,y:3.15,w:2.72,h:1.0,isTextBox:true,margin:0,fontFace:HF,fontSize:54,bold:true,color:GRN,align:'center'});
  s.addText(l,{x,y:4.2,w:2.72,h:0.5,isTextBox:true,margin:0,fontFace:HF,fontSize:13,bold:true,charSpacing:2,color:'AEB6BF',align:'center'});x+=2.9;});
 note(s,'A real approved file. Same ten questions. Completely different life.');})();
ask('Type YES if you want your\nfile to look like that.','ASK #11 — THE PIVOT from agreeing to WANTING. Most important ask before the offer: the first time they state a desire instead of confirming a fact. Do not skip it, do not rush it.');
statement('The software does all of this\nin about a minute.','And that\'s only one of six things people use it for.',{size:46});

/* ================= ACT 4 ================= */
divider('SIX WAYS PEOPLE USE THIS','Three on yourself. Three to get paid.','Some of you came here tonight for the first three. Nobody told you the last three existed.');
ask('Type the number you came\nhere for tonight — 1, 2, or 3.','ASK #12 — primes them to hunt for their own number, which keeps all six avatars watching the rest of the act.');
divider('FIRST — USE IT ON YOURSELF','');
bullets('1 · ANALYZE YOUR PROFILE',['Know your factors — not just your score','What is actually on all three bureaus','What is helping and what is holding you back','Whether you should apply at all'],{n:'Your score is a summary. Your factors are the reasons. Lenders read the reasons.'});
bullets('2 · IMPROVE YOUR PROFILE',['Dispute with the latest AI','Custom letters written per account — not templates','Printed and mailed for you','Every removal tracked'],{n:'Template letters get template responses. The bureaus have seen the same letter ten thousand times — that is how you end up with stall letters.'});
bullets('3 · KNOW WHERE TO APPLY',['Which banks','Which bureau they pull','What order to apply in','Not "apply and hope"'],{n:'Remember the slide where you could not tell me which bureau your last denial pulled. This is what fixes that permanently.'});
statement('Now — here\'s what most people\nin this room don\'t know.','',{dark:true,size:48,n:'Beat. Then move.'});
divider('THEN — USE IT TO GET PAID','The same tool that fixes your file is a business.');
ask('Type YES if you\'d want to get paid\ndoing this for other people.','ASK #13 — opens the second tier and measures how operator-minded the room is. Big YES wall: slow down on the next two. Thin: move through them and spend the time on referrals.');
bullets('4 · LAUNCH A CREDIT REPAIR BUSINESS',['Pull a client\'s report','Read their ten lines','Show them the red on their own screen','Let the software write and mail the letters'],{n:'The consultation sells itself — you show them their own file and ask one question. BE STRAIGHT: credit repair is a regulated business with state requirements. The software is the engine, not the license.'});
bullets('5 · LAUNCH A FUNDING BUSINESS',['Qualify the client before you ever apply','Know the banks, the bureaus, the order','Get paid a percentage of what you get funded'],{n:'This is what people charge ten and fifteen percent for. The hard part was never the paperwork — it was knowing whether the file could get approved before you burned an inquiry finding out. NO EARNINGS CLAIMS.'});
bullets('6 · REFER IT',['Your own referral link','Share the software','Earn on it every month it stays active'],{n:'You do not have to run a single client file to benefit. If all you ever do is send it to people in your circle who keep getting denied, that is a real thing.'});
bullets('ALL SIX. ONE LOGIN.',['Analyze your profile','Improve it with AI disputes','Know where to apply','Launch a credit repair business','Launch a funding business','Refer it and earn'],{num:true,bh:0.6,fs:18,n:'Find yourself on this list. Most of you are on it twice.'});
ask('Type every number that applies\nto you. Not one — all of them.','ASK #14 — someone typing "1, 3, 6" is telling you and themselves that this is worth more than one thing to them. That multiplies perceived value right before the stack.');

/* ================= ACT 5 — THE OFFER ================= */
compare('THE TWO FILES','NOT ELIGIBLE',['14 inquiries','Collections + charge-offs','101% utilization','Approval odds: −$5,000'],'FUNDABLE',['1 inquiry','0 collections','2% utilization','Every line green'],'Same ten questions. Different life.');
statement('Which one are you?','',{dark:true,size:76,n:'Be honest with yourself. Most of this room is the file on the left. That is not a character flaw — it is a starting point, and now it is a measurable one.'});
statement('The gap between those two files\nisn\'t willpower.','It\'s a checklist and a tool.',{size:48});
bullets('THREE LEVERS',['Pay down what\'s high — often $7–8 a week','Remove what shouldn\'t be there','Only apply where you\'re actually eligible'],{num:true,n:'Three levers. The third one is free — it just requires knowing something you did not know an hour ago.'});
ask('Type YES if $8 a week\nis doable for you.','ASK #15 — the last micro-yes before money enters the room. They have just agreed the fix is affordable. That is the frame you want them holding when the price appears four slides later.');
statement('The house.\nThe car.\nThe capital.','Or a business of your own.',{size:56,ls:64,n:'Because that is what this was always about. Not the score.'});
statement('All six.\nOne login.','',{dark:true,size:70});
ask('Type YES if you\'d want all six\nof those in one place.','ASK #16 — agreement on the bundle before it has a price. Now the stack is answering "how much," not "whether."');

/* value stack — native chart */
(function(){const s=S();dots(s,X,0.85);H(s,'WHAT YOU GET',{y:1.2,size:40,h:0.8});
 s.addChart(p.ChartType.bar,[{name:'Value',labels:['Client Summary PDF','Progress Report + Timeline','Letter Print + Certified Mail','AI Dispute Letter Engine','Bank + Bureau Matching','Underwriting Blueprint','AI Credit File Analysis'],values:[45,67,97,97,197,197,297]}],
  {x:X,y:2.15,w:CW,h:4.0,barDir:'bar',chartColors:[INK],showValue:true,dataLabelPosition:'outEnd',dataLabelFormatCode:'"$"#,##0',dataLabelColor:INK,dataLabelFontSize:13,dataLabelFontBold:true,
   showLegend:false,showTitle:false,catAxisLabelColor:SLATE,catAxisLabelFontSize:13,valAxisHidden:true,valGridLine:{style:'none'},catGridLine:{style:'none'},valAxisMaxVal:360,barGapWidthPct:45});
 note(s,'Build it line by line. Name each one and tie it to the use case it powers. Nothing here should be new information by now.');})();
price(null,'$997','TOTAL VALUE',{color:W,n:'Let it sit. Say nothing for a beat.'});
price('$997','$497','',{color:W});
price('$497','$247','',{color:W});
price('$247','$1 TO GET STARTED','7 days, then $97/month',{size:74,color:GRN,subSize:28,n:'One dollar to get started. Seven days. After that it is $97 a month — your card gets charged $97 on [STATE THE EXACT DATE]. No surprises, no small print. If it is not for you, cancel inside the seven days.'});
ask('Type YES if you\'re\ngetting started tonight.','ASK #17 — THE COMMITMENT. Every yes before this one was practice for this one. Wait through the silence — it always feels longer than it is.');
bullets('WHAT HAPPENS IN THOSE 7 DAYS',['Tonight: upload your report','Tonight: run the Blueprint','Tonight: see your ten lines','This week: know whether you\'re eligible — before you apply to anything else'],{num:true,bh:0.7,n:'The trial is not "poke around and see." You have one job in seven days: find out what your own ten lines actually say.'});
bullets('WHO THIS IS FOR',['You\'ve been denied and never got a real answer','You\'re about to apply for something that matters','You\'re fixing your file and want the work tracked','You want to start a credit repair business','You want to start a funding business','You want to refer it and earn'],{bh:0.6,fs:18,n:'Read all six out loud, slowly. Every person in the room should hear their own line.'});
bullets('WHO THIS ISN\'T FOR',['Anyone looking for a guaranteed approval','Anyone who wants someone else to care about their file more than they do'],{bh:0.85,n:'I would rather you not start than start expecting a miracle. This is a tool. A very good one. It is not magic, and it is not a license.'});
bullets('HOW TO START',['Click the link','Create your account — $1','Upload your report tonight'],{num:true,bh:0.85,n:'Say the link out loud. Have someone drop it in chat now, and again in five minutes.'});
statement('[ YOUR LINK HERE ]','',{dark:true,size:52,n:'REPLACE WITH YOUR REFERRAL LINK. Test it logged-out before going live — confirm it charges $1, runs 7 days, and rebills at $97.'});
ask('Type GOT IT when\nyou see the link.','ASK #18 — two jobs at once: confirms the link actually reached people, and puts visible evidence in the chat that others are moving. That is the most persuasive thing on screen at this moment.');
price('$247','$1 TO GET STARTED','7 days, then $97/month  ·  [ YOUR LINK ]',{size:70,color:GRN,subSize:24,n:'CLOSE BEFORE THE DEMO. "You were never bad with credit — you were playing a game nobody showed you the rules to. Get started now, then watch me use the exact thing you just got. Everybody else: watch anyway, and decide at the end."'});

/* ================= DEMO ================= */
divider('LIVE DEMO','Slides off. The link stays on screen.','DEMO RULES: no live pulls — files pre-pulled hours ahead. Full-resolution screenshots of every beat as backup. Everything anonymized. Never demo a module you know is broken. If the platform stalls, move to screenshots without announcing it. Cut beats from the end, never the Blueprint. BEATS: 1 upload · 2 AI file analysis · 3 Blueprint live · 4 personals mismatch · 5 utilization 101% · 6 paydown calculator · 7 negative items · 8 AI letters · 9 print + certified mail · 10 progress report · 11 bank + bureau matching · 12 client/consultation view · 13 referral link · 14 a green file. Call the use-case number out loud on every beat.');
ask('Type YES if you want to see\nyour own ten lines.','DEMO ASK — after beat 3 (the Blueprint live).');
ask('Type YES if you thought that\nnumber would be higher.','DEMO ASK — after beat 6 (the paydown calculator).');
ask('Type YES if that was\nhelpful tonight.','DEMO ASK — after beat 14 (the green file). This one warms them for the second ask.');
price(null,'$1 TO GET STARTED','7 days, then $97/month  ·  [ YOUR LINK ]',{size:74,color:GRN,subSize:24,n:'THE SECOND ASK. This is what actually converts the room — do not rush past it into questions. Everyone undecided forty-five minutes ago just watched it work. Say the price, say the rebill date, say the link, then give fifteen seconds of silence before you take the first question.'});
ask('Type YES if you\'re in.','ASK #22 — the second ask. Fifteen seconds of silence after it.');

/* ================= Q&A ================= */
(function(){const s=S(true);dots(s,X,0.85);
 s.addText('QUESTIONS',{x:X,y:1.2,w:CW,h:1.0,isTextBox:true,margin:0,fontFace:HF,fontSize:52,bold:true,color:W});
 const L=['700 score?','Under 30% utilization?','5 cards, 2 yrs history?','3 cards, 3 yrs, $5,000?','4+ new accounts / 12 mo?','Under 4 inquiries?','Collections?','Charge-offs?','Late payments?','Bankruptcy?'];
 s.addText('THE BLUEPRINT',{x:X,y:2.35,w:5.4,h:0.4,isTextBox:true,margin:0,fontFace:HF,fontSize:13,bold:true,charSpacing:2,color:GOLD});
 let y=2.85;L.forEach((l,i)=>{s.addText(`${i+1}.  ${l}`,{x:X,y,w:5.4,h:0.34,isTextBox:true,margin:0,fontFace:BF,fontSize:15,color:'D8DCE1'});y+=0.34;});
 s.addShape(p.ShapeType.roundRect,{x:X+6.3,y:2.35,w:5.3,h:3.3,rectRadius:0.14,fill:{color:'16181C'},line:{color:GRN,width:2}});
 s.addText('$1 TO GET STARTED',{x:X+6.3,y:3.0,w:5.3,h:0.9,isTextBox:true,margin:0,fontFace:HF,fontSize:34,bold:true,color:GRN,align:'center'});
 s.addText('7 days, then $97/month',{x:X+6.3,y:3.95,w:5.3,h:0.5,isTextBox:true,margin:0,fontFace:BF,fontSize:20,color:'C9CFD6',align:'center'});
 s.addText('[ YOUR LINK ]',{x:X+6.3,y:4.55,w:5.3,h:0.5,isTextBox:true,margin:0,fontFace:BF,fontSize:18,color:GOLD,align:'center'});
 note(s,'Leave this up the entire Q&A. Late arrivals can still read the Blueprint and still find the link.');})();

p.writeFile({fileName:'Score-Machine-Masterclass.pptx'}).then(()=>console.log('slides:',N));
