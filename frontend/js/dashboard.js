async function load(){
  const [s,c] = await Promise.all([fetch("/api/dashboard/stats").then(r=>r.json()),fetch("/api/privacy-checklist").then(r=>r.json())]);
  document.getElementById("stats").innerHTML = `<div class="card"><h3>Total Assessments</h3><div class="risk">${s.total_assessments}</div></div>
  <div class="card"><h3>Average Score</h3><div class="risk">${s.average_score}</div></div>
  <div class="card"><h3>Interpretation</h3><p>Higher score = higher assessed exposure/risk.</p></div>`;
  document.getElementById("checklist").innerHTML=c.checklist.map(x=>`<li>□ ${x}</li>`).join("");
  new Chart(document.getElementById("dist"),{type:"bar",data:{labels:Object.keys(s.risk_distribution),datasets:[{label:"Assessments",data:Object.values(s.risk_distribution)}]},options:{responsive:true}});
}
load();
