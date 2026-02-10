<div class="tab_section" id="buttons">
    <nav>
        <button class='tab1'>Home</button>
        <button class='tab2'>FAQ</button>
        <button class='tab3'>Guideline</button>    
        <button class='tab4'>Support</button>
    </nav>
</div>

<script>
const pages = {
    "Home": "Home.html",
    "FAQ": "FAQ.html",
    "About Us": "About.html",
    "Support": "Support.html",
    "Submit Grades": "Submit_Grades.html",
    "My Shortlist": "My_Shortlist.html",
};

const allButtons = document.querySelectorAll('#buttons nav button');
allButtons.forEach(btn => {
    const buttonText = btn.textContent.trim(); 
    if (pages[buttonText]) {
        btn.onclick = () => { window.location.href = pages[buttonText]; };
    }
});
</script>
