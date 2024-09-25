   const tapButton = document.getElementById('tap-button');
   const startButton = document.getElementById('start-button');
   const stopButton = document.getElementById('stop-button');

   function updateDisplay(users) {
       for (const hamster in users) {
           document.getElementById(`level${hamster[hamster.length - 1]}`).innerText = users[hamster].level;
           document.getElementById(`xp${hamster[hamster.length - 1]}`).innerText = users[hamster].xp;
       }
   }

   tapButton.addEventListener('click', async () => {
       const response = await fetch('/tap', { method: 'POST' });
       const json = await response.json();
       updateDisplay(json);
   });

   startButton.addEventListener('click', async () => {
       await fetch('/start', { method: 'POST' });
   });

   stopButton.addEventListener('click', async () => {
       await fetch('/stop', { method: 'POST' });
   });

   const updateStatus = async () => {
       const response = await fetch('/status');
       const json = await response.json();
       updateDisplay(json.users);
   };

   setInterval(updateStatus, 1000); // Update every second
