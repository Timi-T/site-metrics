// Query all the sites

const { fetch } = require('node-fetch');

//import fetch from 'node-fetch';

let a = 1;
while (a < 2) {
  /* ============= Project 1 =============== */
  // Query producktiv backend || Method: POST
  const info = { 'email': 'ope@gmail', 'login_password': 'opeyemi' }
  fetch('https://producktiv-backend.onrender.com',
    {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(info),
    }
  )
  .then((data) => {
    console.log(data);
  });
  a = 3;

  // Query producktiv frontend || Method: GET
  //fetch('https://producktiv.onrender.com');
  /* ============= END =============== */

  /* ============= Project 2 =============== */
  // Query fees-manager frontend || Method: GET
  //fetch('https://fees-manager.onrender.com');
  /* ============= END =============== */

  /* ============= Project 3 =============== */
  // Query schfees-manager || Method: POST
  //fetch('https://schfees-manager.onrender.com/login');
  /* ============= END =============== */

  /* ============= Project 4 =============== */
  // Query airbnb clone || Method: GET
  /* ============= END =============== */

  /* ============= Portfolio project =============== */
  // Query portfolio site || Method: GET
  //fetch('https://ogunbode-portfolio.onrender.com');
  /* ============= END =============== */
}