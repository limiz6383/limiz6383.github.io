const resume = document.getElementById("resume");
function redirectToResume() {
    window.open("https://drive.google.com/file/d/1G-Drv22aJmnsn63mW9YQ6vdUcdJzUSFb/view?usp=sharing", "_blank");
}
resume.addEventListener("click", redirectToResume);

const email = document.getElementById("email");
function emailbuttonclick(event) {
    event.preventDefault();
    const emailAddress = "limizuho@berkeley\.edu"
    const mailtoLink = `mailto:${emailAddress}`;
    window.location.href= mailtoLink;
}

email.addEventListener("click", emailbuttonclick);