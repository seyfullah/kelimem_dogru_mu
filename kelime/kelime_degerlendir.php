    <?php
    $image = $_POST['image'];
    $image = explode(',', $image);
    $image = $image[1];

    $url = "";

    $json = json_encode(['image' => $image]);
    $json = str_replace(PHP_EOL, '', $json);
    $json = str_replace(" ", '+', $json);

    $options = ['http' => [
        'method' => 'POST',
        'header' => 'Content-type:application/json',
        'content' => $json
    ]];

    $context = stream_context_create($options);
    $response = file_get_contents($url, false, $context);
    $response = str_replace(array("'", '"'), '', $response);

    echo $response . "<br/>";

    $result = "Okunan kelime listede bulunamadi.";
    $rowIndex = 0;
    $rowCount = 85;
    if (($handle = fopen("Kelimeler.csv", "r")) !== false) {
        while (($data = fgetcsv($handle, $rowCount, ",")) !== false) {
            if (strcmp($data[0], $response) == 0) {
                $result = "Yanlış cevap. Doğrusu: " . $data[1];
            } elseif (strcmp($data[1], $response) == 0) {
                $result = "Doğru cevap";
            }
        }
        fclose($handle);
    }

    echo $result;
