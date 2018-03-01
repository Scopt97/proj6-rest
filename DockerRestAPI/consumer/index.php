<html>
    <head>
        <title>CIS 322 REST-api: Brevets</title>
    </head>

    <body>
        <h1>List of brevets</h1>
        <ul>
            <?php
            $json = file_get_contents('http://api-service/');
            $obj = json_decode($json);
	          $brevets = $obj->All; //TODO change to Brevets later
            foreach ($brevets as $b) {
                echo "<li>$b</li>";
            }
            ?>
        </ul>
    </body>
</html>
