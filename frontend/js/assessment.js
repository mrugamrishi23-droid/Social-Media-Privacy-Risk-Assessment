let questions = [];
let lastAnswers = {};
const form = document.getElementById("assessmentForm");
const result = document.getElementById("result");

async function loadQuestions(){
  const res = await fetch("/api/questions");
  const data = await res.json();
  questions = data.questions;
  let current = "";
  questions.forEach(q => {
    if(q.category !== current){
      current = q.category;
      form.insertAdjacentHTML("beforeend", `<h2>${current.replaceAll("_"," ").toUpperCase()}</h2>`);
    }
    let input = "";
    if(q.type === "yesno"){
      input = `<label><input type="radio" name="${q.id}" value="true" required> Yes</label>
               <label><input type="radio" name="${q.id}" value="false"> No</label>`;
    } else {
      input = q.options.map((o,i)=>`<label><input type="radio" name="${q.id}" value="${o}" ${i===0?"required":""}> ${o}</label>`).join("");
    }
    form.insertAdjacentHTML("beforeend", `<div class="question"><strong>${q.id.toUpperCase()}.</strong> ${q.text}<div>${input}</div></div>`);
  });
}
function readAnswers(){
  const data = {};
  for(const q of questions){
    const selected = document.querySelector(`input[name="${q.id}"]:checked`);
    if(!selected) throw new Error(`Please answer ${q.id}.`);
    data[q.id] = q.type === "yesno" ? selected.value === "true" : selected.value;
  }
  return data;
}
document.getElementById("submitBtn").onclick = async e => {
  e.preventDefault();
  try{
    const answers = readAnswers(); lastAnswers = answers;
    const res = await fetch("/api/assessment",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({answers})});
    const data = await res.json();
    if(!res.ok) throw new Error((data.errors||[data.error]).join(", "));
    result.innerHTML = `<div class="card"><h2>Assessment Result</h2><div class="score">${data.overall_score}/100 <small>${data.risk_level}</small></div>
    <p>${data.disclaimer}</p><h3>Category Scores</h3><ul>${Object.entries(data.category_scores).map(([k,v])=>`<li>${k.replaceAll("_"," ")}: <strong>${v}</strong></li>`).join("")}</ul>
    <h3>Top Findings</h3>${data.findings.map(f=>`<div class="finding"><strong>${f.severity} — ${f.finding_type}</strong><br>${f.description}</div>`).join("") || "<p>No high-priority findings were triggered.</p>"}
    <h3>Recommendations</h3><ul>${data.recommendations.map(r=>`<li><strong>${r.priority}:</strong> ${r.recommendation}</li>`).join("")}</ul>
    <p><a class="button" href="/api/report/${data.assessment_id}" target="_blank">Open Privacy Report</a> <a class="button" href="/dashboard">Dashboard</a></p></div>`;
    window.scrollTo({top:document.body.scrollHeight,behavior:"smooth"});
  }catch(err){result.innerHTML=`<p class="error">${err.message}</p>`}
};
loadQuestions();
