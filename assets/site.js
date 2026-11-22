// Contact button: the address is never present in the HTML or this file as one string.
// It is assembled from character codes only when someone clicks, so scrapers find nothing.
(function () {
  var parts = [[112, 97, 116, 114, 105, 99, 107], [112, 103, 99, 111, 110, 115, 117, 108, 116, 105, 110, 103], [99, 97]];
  function addr() {
    var s = parts.map(function (p) { return String.fromCharCode.apply(null, p); });
    return s[0] + String.fromCharCode(64) + s[1] + "." + s[2];
  }
  document.querySelectorAll("[data-contact]").forEach(function (el) {
    el.addEventListener("click", function (e) {
      e.preventDefault();
      var a = addr();
      var subject = el.getAttribute("data-subject") || "";
      var href = "mai" + "lto:" + a + (subject ? "?subject=" + encodeURIComponent(subject) : "");

      // Always show the address too: if the visitor has no default mail app
      // (common with webmail), the mailto link silently does nothing.
      var box = el.parentNode.querySelector(".contact-reveal");
      if (!box) {
        box = document.createElement("p");
        box.className = "contact-reveal";
        var link = document.createElement("a");
        link.href = href;
        link.textContent = a;
        var copy = document.createElement("button");
        copy.type = "button";
        copy.textContent = "Copy";
        copy.addEventListener("click", function () {
          var done = function () { copy.textContent = "Copied"; };
          if (navigator.clipboard) navigator.clipboard.writeText(a).then(done, function () {});
          else { var r = document.createRange(); r.selectNodeContents(link); getSelection().removeAllRanges(); getSelection().addRange(r); }
        });
        box.appendChild(document.createTextNode("Email us at "));
        box.appendChild(link);
        box.appendChild(copy);
        el.parentNode.insertBefore(box, el.nextSibling);
      }
      window.location.href = href;
    });
  });

  // Highlight the nav item for the section in view (as the Strikingly theme did).
  var links = Array.prototype.slice.call(document.querySelectorAll(".nav a"));
  if (!links.length || !("IntersectionObserver" in window)) return;
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting && byId[en.target.id]) {
        links.forEach(function (a) { a.classList.remove("active"); });
        byId[en.target.id].classList.add("active");
      }
    });
  }, { rootMargin: "-80px 0px -60% 0px" });
  Object.keys(byId).forEach(function (id) { var s = document.getElementById(id); if (s) io.observe(s); });
})();
