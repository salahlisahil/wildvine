"use strict";

const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const tabBtn = document.querySelectorAll(".tab-btn");
const tabContent1 = document.querySelector(".tab-content1");

const tabContent2 = document.querySelector(".tab-content2");

const tabContent3 = document.querySelector(".tab-content3");
const whichOne = "mission";

const navElemArr = [navOpenBtn, navCloseBtn];

for (let i = 0; i < navElemArr.length; i++) {
  navElemArr[i].addEventListener("click", function () {
    navbar.classList.toggle("active");
  });
}

const navbarLinks = document.querySelectorAll("[data-nav-link]");

for (let i = 0; i < navbarLinks.length; i++) {
  navbarLinks[i].addEventListener("click", function () {
    navbar.classList.remove("active");
  });
}

const header = document.querySelector("[data-header]");

window.addEventListener("scroll", function () {
  window.scrollY >= 50
    ? header.classList.add("active")
    : header.classList.remove("active");
});

const tabContents = document.getElementsByClassName("tab-content");
tabContents[1].style.display = "none";
tabContents[2].style.display = "none";
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tab-content");

  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tab-btn");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].classList.remove("active");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.classList.add("active");
}

// // Open the first tab by default
document.getElementById("tab-content1").style.display = "block";
document.getElementsByClassName("tab-btn")[0].classList.add("active");
