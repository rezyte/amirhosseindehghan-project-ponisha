const sections = document.querySelectorAll("section");
const links = document.querySelectorAll("nav .container ul li");

let sectionOne = document.getElementById("fixedBtnCount");

let sticky = sectionOne.offsetTop;

function btnTopFunction() {
  if (window.pageYOffset > sticky) {
    document.getElementById("fixedBtn").style.display = 'inline-block'
  } else {
    document.getElementById("fixedBtn").style.display = 'none'
  }
}
function changeLinkState() {
  let index = sections.length;

  while (--index && window.scrollY + 50 < sections[index].offsetTop) {}

  links.forEach((link) => link.classList.remove("active"));
  links[index].classList.add("active");
}

changeLinkState();
window.addEventListener("scroll", ()=>{
  changeLinkState()
  btnTopFunction()
});

// show more

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
let itemsShow = (el, num, classItem) => {
  for (i = 0; i < num; i++) {
    el[i].classList.remove(classItem);
  }
};
let splide = new Splide("#splide", {
  padding: "5rem",
  direction: "rtl",
  pagination: false,
  rewind: true,
  type: "loop",
});

splide.mount();

let splide2 = new Splide("#splide2", {
  padding: "5rem",
  direction: "rtl",
  pagination: false,
  rewind: true,
  type: "loop",
});

splide2.mount();
