// ---------------- Wing navigation ----------------
const wings = document.querySelectorAll(".wing");
const wards = document.querySelectorAll(".ward");

wings.forEach((btn) => {
  btn.addEventListener("click", () => {
    const target = btn.dataset.wing;
    wings.forEach((w) => w.removeAttribute("aria-current"));
    btn.setAttribute("aria-current", "true");
    wards.forEach((w) => w.classList.toggle("hidden", w.dataset.wing !== target));
  });
});

// ---------------- Helpers ----------------
async function postJSON(url, payload) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await res.json();
  return { ok: res.ok, data };
}

function setNote(name, message, isOk) {
  const el = document.querySelector(`[data-note="${name}"]`);
  el.textContent = message;
  el.classList.toggle("ok", !!isOk);
}

// ---------------- Registration ----------------
document.getElementById("form-register").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const payload = {
    name: form.name.value,
    age: form.age.value,
    patient_id: form.patient_id.value,
  };
  const { ok, data } = await postJSON("/api/patients", payload);
  if (!ok) return setNote("register", data.error, false);

  setNote("register", "Patient registered successfully.", true);
  const p = data.patient;
  document.getElementById("slip-register").innerHTML = `
    <p class="slip-tag-eyebrow">Patient Chart</p>
    <h3 class="slip-headline">${p.name}</h3>
    <dl>
      <div class="slip-row"><dt>Patient ID</dt><dd>${p.patient_id}</dd></div>
      <div class="slip-row"><dt>Age</dt><dd>${p.age}</dd></div>
    </dl>
  `;
  form.reset();
});

// ---------------- Appointments ----------------
const dateInput = document.querySelector('#form-appointment input[name="date"]');
const today = new Date();
const maxDate = new Date();
maxDate.setDate(today.getDate() + 7);
dateInput.min = today.toISOString().slice(0, 10);
dateInput.max = maxDate.toISOString().slice(0, 10);

document.getElementById("form-appointment").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const payload = { department: form.department.value, date: form.date.value };
  const { ok, data } = await postJSON("/api/appointments", payload);
  if (!ok) return setNote("appointment", data.error, false);

  setNote("appointment", "Booking confirmed.", true);
  const a = data.appointment;
  document.getElementById("slip-appointment").innerHTML = `
    <p class="slip-tag-eyebrow">Booking Confirmation</p>
    <h3 class="slip-headline">${a.department}</h3>
    <dl>
      <div class="slip-row"><dt>Date</dt><dd>${a.date_display}</dd></div>
    </dl>
  `;
});

// ---------------- Billing ----------------
document.getElementById("form-billing").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const payload = {
    patient_type: form.patient_type.value,
    num_labtests: form.num_labtests.value,
  };
  const { ok, data } = await postJSON("/api/bill", payload);
  if (!ok) return setNote("billing", data.error, false);

  setNote("billing", "Bill calculated.", true);
  const b = data.bill;
  document.getElementById("slip-billing").innerHTML = `
    <p class="slip-tag-eyebrow">Itemised Bill</p>
    <h3 class="slip-headline">${b.patient_type}</h3>
    <dl>
      <div class="slip-row"><dt>Lab tests</dt><dd>${b.num_labtests} × $10</dd></div>
      <div class="slip-row"><dt>Subtotal</dt><dd>$${b.subtotal.toFixed(2)}</dd></div>
      <div class="slip-total"><dt>Total due</dt><dd>$${b.total.toFixed(2)}</dd></div>
    </dl>
  `;
});

// ---------------- Triage ----------------
const severityRange = document.getElementById("severity-range");
const severityOutput = document.getElementById("severity-output");
severityRange.addEventListener("input", () => {
  severityOutput.textContent = severityRange.value;
});

document.getElementById("form-triage").addEventListener("submit", async (e) => {
  e.preventDefault();
  const payload = { severity: severityRange.value };
  const { ok, data } = await postJSON("/api/triage", payload);
  if (!ok) return setNote("triage", data.error, false);

  setNote("triage", "Room assigned.", true);
  const t = data.triage;
  const calmClass = t.room === "Waiting Room" ? "calm" : "";
  document.getElementById("slip-triage").innerHTML = `
    <p class="slip-tag-eyebrow">Triage Summary</p>
    <h3 class="slip-headline">Severity ${t.severity} / 10</h3>
    <span class="slip-room ${calmClass}">${t.room}</span>
  `;
});
