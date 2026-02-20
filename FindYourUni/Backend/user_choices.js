document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.main_form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        let user_successrate = document.getElementById("success_rate").value;
        let user_satisfaction = document.getElementById("satisfaction").value;
        let user_grades = document.getElementById("gradesAL").value;
        let user_course = document.getElementById("coursename").value;
        let user_country = document.getElementById("country").value;
        let ucas_points = 0;
        if (user_grades == "A*A*A*"){
            ucas_points = 56*3;
        } else if (user_grades == "A*A*A") {
            ucas_points = (56*2) + 48;
        } else if (user_grades == "A*AA") {
            ucas_points = 56 + (48*2);
        } else {
            alert("Please input for AL grades more than A*AA, for now :)");
            return;
        }

        fetch('http://127.0.0.1:5000/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // tell Flask to expect JSON
            },
            body: JSON.stringify({
                points : ucas_points,
                country : user_country,
                course : user_course,
                successrate : user_successrate,
                student_satisfaction : user_satisfaction
            })
        })
        .then(response => response.json()) // Wait for Python's response
        .then(data => {


            const listElement = document.getElementById("uni-list");
            listElement.innerHTML = "";
    
            data.forEach(course => {
            let li = document.createElement("li");
        
            // This keeps your exact format but adds the specific data points
            li.innerHTML = `University: ${course.UNIVERSITY_NAME} | Course: ${course.COURSE_NAME} | <a href="${course.COURSE_URL}" target="_blank">${course.COURSE_URL}</a>`;

            listElement.appendChild(li);
            });

        })
        .catch((error) => {
            alert("Connection failed :(");
        });
    })
});
