// dashboard-charts.js

// Wait for the document to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
 // Sample Data for the chart (you can replace it with actual data)
 const moodData = {
  labels: ['Anxiety', 'Depression', 'Schizophrenia', 'Bipolar Disorder'],
  datasets: [{
   label: 'Mental Health Assessment',
   data: [45, 67, 23, 39], // Example data, replace with dynamic data
   backgroundColor: [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)'
   ],
   borderColor: [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)'
   ],
   borderWidth: 1
  }]
 };

 // Configuration options for the chart
 const config = {
  type: 'bar',  // Change 'bar' to 'line', 'pie', etc. based on your needs
  data: moodData,
  options: {
   responsive: true,
   scales: {
    y: {
     beginAtZero: true
    }
   }
  }
 };

 // Render the chart in the specified canvas
 const ctx = document.getElementById('moodChart').getContext('2d');
 new Chart(ctx, config);  // Creating a new Chart instance
});

