<?php

include('/var/www/html/config.php');

$conn = new mysqli($host, $user, $pass, $db);

if($conn->connect_error) {
	die("Connection failed " . $conn->connect_error);
} 

echo "test" . "<br><br>";

$sql = "SELECT id, firstname, lastname FROM gebruikers";

$result = $conn->query($sql);

if($result->num_rows > 0){
	while($row = $result->fetch_assoc()) {
		echo "id: " . $row["id"] . " - Name: " . $row["firstname"] . " " . $row["lastname"] . "<br>";
	}

} else {
	echo "No results!";
}


?>

