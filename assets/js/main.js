/* Jed's Party Services — site behaviour (no dependencies) */
(function () {
  "use strict";

  document.documentElement.classList.remove("no-js");

  /* ---------- Header: solid on scroll, mobile menu ---------- */
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");

  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 24);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  function setMenu(open) {
    if (!header || !toggle) return;
    header.classList.toggle("is-open", open);
    document.body.classList.toggle("nav-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }
  if (toggle) {
    toggle.addEventListener("click", function () {
      setMenu(toggle.getAttribute("aria-expanded") !== "true");
    });
    document.querySelectorAll(".nav a").forEach(function (a) {
      a.addEventListener("click", function () { setMenu(false); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setMenu(false);
    });
    window.matchMedia("(min-width: 921px)").addEventListener("change", function (mq) {
      if (mq.matches) setMenu(false);
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!("IntersectionObserver" in window) || reduce) {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ---------- Staffing estimator (services page) ---------- */
  var est = document.querySelector("[data-estimator]");
  if (est) {
    var RATE_SERVER = 40;
    var RATE_BAR = 50;
    var MIN_HOURS = 4;
    var guests = est.querySelector("#est-guests");
    var hours = est.querySelector("#est-hours");
    var outGuests = est.querySelector("[data-out='guests']");
    var outHours = est.querySelector("[data-out='hours']");
    var rowServers = est.querySelector("[data-row='servers']");
    var rowBar = est.querySelector("[data-row='bartenders']");
    var rowCoord = est.querySelector("[data-row='coordinator']");
    var total = est.querySelector("[data-out='total']");
    var money = function (n) { return "$" + n.toLocaleString("en-US"); };
    var range = function (lo, hi, unit) {
      return (lo === hi ? lo : lo + "–" + hi) + " " + unit + (hi === 1 ? "" : "s");
    };

    function paintTrack(input) {
      var pct = ((input.value - input.min) / (input.max - input.min)) * 100;
      input.style.setProperty("--fill", pct + "%");
    }

    function update() {
      var g = Number(guests.value);
      var h = Math.max(MIN_HOURS, Number(hours.value));
      var service = est.querySelector("input[name='est-service']:checked").value;
      outGuests.textContent = g;
      outHours.textContent = h + " hrs";
      paintTrack(guests);
      paintTrack(hours);

      // 1 server per 15–25 guests; 1 bartender per 30–50 guests
      var sLo = Math.max(1, Math.ceil(g / 25)), sHi = Math.max(1, Math.ceil(g / 15));
      var bLo = Math.max(1, Math.ceil(g / 50)), bHi = Math.max(1, Math.ceil(g / 30));
      var useS = service !== "bar", useB = service !== "server";

      rowServers.hidden = !useS;
      rowBar.hidden = !useB;
      rowServers.lastElementChild.textContent = range(sLo, sHi, "server");
      rowBar.lastElementChild.textContent = range(bLo, bHi, "bartender");

      var lo = (useS ? sLo * RATE_SERVER : 0) + (useB ? bLo * RATE_BAR : 0);
      var hi = (useS ? sHi * RATE_SERVER : 0) + (useB ? bHi * RATE_BAR : 0);
      lo *= h; hi *= h;
      total.textContent = lo === hi ? money(lo) : money(lo) + " – " + money(hi);

      var staffHi = (useS ? sHi : 0) + (useB ? bHi : 0);
      rowCoord.hidden = staffHi < 6;
    }

    est.addEventListener("input", update);
    est.addEventListener("change", update);
    update();
  }

  /* ---------- Event request form → pre-filled email ---------- */
  var form = document.querySelector("[data-request-form]");
  if (form) {
    var status = form.querySelector(".form__status");
    var to = form.getAttribute("data-mailto");

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var firstInvalid = null;
      form.querySelectorAll("[required]").forEach(function (field) {
        var ok = field.checkValidity();
        field.setAttribute("aria-invalid", ok ? "false" : "true");
        if (!ok && !firstInvalid) firstInvalid = field;
      });
      if (firstInvalid) { firstInvalid.focus(); return; }

      var v = function (name) {
        var el = form.elements[name];
        return el ? String(el.value).trim() : "";
      };
      var name = (v("first") + " " + v("last")).trim();
      var subject = "Event Request: " + v("event") + " on " + v("date") + " (" + name + ")";
      var body = [
        "Name: " + name,
        "Phone: " + v("phone"),
        "Email: " + v("email"),
        "Type of event: " + v("event"),
        "Service: " + v("service"),
        "Number of guests: " + v("guests"),
        "City of event: " + v("city"),
        "Date of event: " + v("date"),
        "",
        "Details:",
        v("message") || "(none)"
      ].join("\n");

      window.location.href = "mailto:" + to +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);
      if (status) {
        status.classList.add("is-visible");
        status.focus();
      }
    });

    form.addEventListener("input", function (e) {
      if (e.target.getAttribute("aria-invalid") === "true" && e.target.checkValidity()) {
        e.target.setAttribute("aria-invalid", "false");
      }
    });
  }
})();
