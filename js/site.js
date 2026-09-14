(() => {
  const root = document.documentElement;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const spotlight = () => {
    let px = window.innerWidth * 0.5;
    let py = 120;
    let tx = px;
    let ty = py;
    let running = false;

    const loop = () => {
      px += (tx - px) * 0.14;
      py += (ty - py) * 0.14;
      root.style.setProperty("--px", `${px}px`);
      root.style.setProperty("--py", `${py}px`);
      if (Math.abs(tx - px) + Math.abs(ty - py) > 0.35) {
        requestAnimationFrame(loop);
      } else {
        running = false;
      }
    };

    window.addEventListener(
      "pointermove",
      (event) => {
        tx = event.clientX;
        ty = event.clientY;
        if (!running) {
          running = true;
          requestAnimationFrame(loop);
        }
      },
      { passive: true },
    );
  };

  const reveal = () => {
    const nodes = [...document.querySelectorAll(".reveal")];
    if (reduce) {
      nodes.forEach((node) => node.classList.add("is-in"));
      return;
    }

    const io = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      },
      { threshold: 0.18, rootMargin: "0px 0px -10% 0px" },
    );

    nodes.forEach((node, index) => {
      node.style.setProperty("--delay", `${Math.min(index * 55, 280)}ms`);
      io.observe(node);
    });
  };

  spotlight();
  reveal();
})();
