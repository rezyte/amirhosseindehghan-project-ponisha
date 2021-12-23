let itemsShow = (el, num, classItem) => {
  for (i = 0; i < num; i++) {
    el[i].classList.remove(classItem);
  }
};
window.addEventListener("load", () => {
  const elDays = document.querySelector(".days");
  const elHours = document.querySelector(".hours");
  const elMinutes = document.querySelector(".minutes");
  const elSeconds = document.querySelector(".seconds");

  let timeLeft = {
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0,
  };

  let totalSeconds = 0;

  // let futureDate = new Date();
  let futureDate = new Date('Tue Dec 31 2021 00:00:01 GMT+03:30');
  // futureDate.setDate(futureDate.getDate() + 14);

  function init() {
    totalSeconds = Math.floor((futureDate - new Date()) / 1000);
    setTimeLeft();
    let interval = setInterval(() => {
      if (totalSeconds < 0) {
        clearInterval(interval);
      }
      countTime();
    }, 1000);
  }

  function countTime() {
    if (totalSeconds > 0) {
      --timeLeft.seconds;
      if (timeLeft.minutes >= 0 && timeLeft.seconds < 0) {
        timeLeft.seconds = 59;
        --timeLeft.minutes;
        if (timeLeft.hours >= 0 && timeLeft.minutes < 0) {
          timeLeft.minutes = 59;
          --timeLeft.hours;
          if (timeLeft.days >= 0 && timeLeft.hours < 0) {
            timeLeft.hours = 23;
            --timeLeft.days;
          }
        }
      }
    }
    --totalSeconds;
    printTime();
  }

  function printTime() {
    animateFlip(elDays, timeLeft.days);
    animateFlip(elHours, timeLeft.hours);
    animateFlip(elMinutes, timeLeft.minutes);
    animateFlip(elSeconds, timeLeft.seconds);
  }

  function animateFlip(element, value) {
    const valueInDom = element.querySelector(".bottom-back").innerText;
    const currentValue = value < 10 ? "0" + value : "" + value;

    if (valueInDom === currentValue) return;

    element.querySelector(".top-back span").innerText = currentValue;
    element.querySelector(".bottom-back span").innerText = currentValue;

    gsap.to(element.querySelector(".top"), 0.7, {
      rotationX: "-180deg",
      transformPerspective: 300,
      ease: Quart.easeOut,
      onComplete: function () {
        element.querySelector(".top").innerText = currentValue;
        element.querySelector(".bottom").innerText = currentValue;
        gsap.set(element.querySelector(".top"), { rotationX: 0 });
      },
    });

    gsap.to(element.querySelector(".top-back"), 0.7, {
      rotationX: 0,
      transformPerspective: 300,
      ease: Quart.easeOut,
      clearProps: "all",
    });
  }

  function setTimeLeft() {
    timeLeft.days = Math.floor(totalSeconds / (60 * 60 * 24));
    timeLeft.hours = Math.floor((totalSeconds / (60 * 60)) % 24);
    timeLeft.minutes = Math.floor((totalSeconds / 60) % 60);
    timeLeft.seconds = Math.floor(totalSeconds % 60);
  }

  init();
});

let showMore = (classItemDot, classItem) => {
  let hideTd = document.querySelectorAll(classItemDot);
  if (hideTd.length >= 3) {
    itemsShow(hideTd, 3, classItem);
  } else {
    itemsShow(hideTd, hideTd.length, classItem);
  }
  if (hideTd.length === 0) {
    alert("آیتمی برای نمایش وجود ندارد");
  }
};

let sectionOne = document.getElementById("fixedBtnCount");

let sticky = sectionOne.offsetTop;

function btnTopFunction() {
  if (window.pageYOffset > sticky) {
    document.getElementById("fixedBtn").style.display = "inline-block";
  } else {
    document.getElementById("fixedBtn").style.display = "none";
  }
}
function changeLinkState() {
  let index = sectionsCount.length;
  while (--index && window.scrollY + 50 < sectionsCount[index].offsetTop) {}

  links.forEach((link) => link.classList.remove("active"));
  links[index].classList.add("active");
  console.log(index);
  console.log(links[index]);
}

let isMobile = window.matchMedia("only screen and (min-width: 992px)").matches;
if (isMobile) {
  const sections = document.querySelectorAll("section");
  const navLi = document.querySelectorAll("nav .container ul li");
  window.onscroll = () => {
    var current = "";

    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      if (window.pageYOffset >= sectionTop - 60) {
        current = section.getAttribute("id");
      }
    });

    navLi.forEach((li) => {
      li.classList.remove("active");
      if (li.classList.contains(current)) {
        li.classList.add("active");
      }
    });
  };
}

function addActive(self) {
  [].forEach.call(document.querySelectorAll("nav ul li"), function (el) {
    el.classList.remove("active");
  });

  self.classList.add("active");
}

window.addEventListener("scroll", () => {
  btnTopFunction();
});
