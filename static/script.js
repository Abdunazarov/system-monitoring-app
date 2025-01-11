let recording = false;
let timer = 0;
let interval;


async function fetchMetrics() {
    const response = await fetch('/metrics');
    const data = await response.json();

    document.getElementById('cpu').textContent = data.cpu_usage.toFixed(1);
    document.getElementById('ram_free').textContent = data.ram_free.toFixed(2);
    document.getElementById('ram_total').textContent = data.ram_total.toFixed(2);
    document.getElementById('disk_free').textContent = data.disk_free.toFixed(2);
    document.getElementById('disk_total').textContent = data.disk_total.toFixed(2);
}


document.getElementById('start').addEventListener('click', async () => {
    await fetch('/start-recording', { method: 'POST' }); 

    recording = true;
    document.getElementById('start').style.display = 'none';
    document.getElementById('stop').style.display = 'block';

    interval = setInterval(() => {
        timer++;
        document.getElementById('timer').textContent = `Время записи: ${timer} сек`;
    }, 1000);
});


document.getElementById('stop').addEventListener('click', () => {
    recording = false;
    document.getElementById('start').style.display = 'block';
    document.getElementById('stop').style.display = 'none';
    clearInterval(interval);
    timer = 0;
    document.getElementById('timer').textContent = "";
});


document.getElementById('history').addEventListener('click', async () => {
    const response = await fetch('/history'); 
    const data = await response.json();

    const historyTable = document.getElementById('history-table');
    historyTable.innerHTML = `
        <tr>
            <th>Время</th>
            <th>ЦП (%)</th>
        </tr>
    `;

    data.forEach(record => {
        const row = historyTable.insertRow();
        row.insertCell(0).textContent = new Date(record.timestamp).toLocaleString();
        row.insertCell(1).textContent = record.cpu_usage.toFixed(1);
    });

    document.getElementById('history-container').style.display = 'block';
});

setInterval(fetchMetrics, 1000);
fetchMetrics();
