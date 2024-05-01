<!DOCTYPE html>
<html lang="tr">

<head>
    <title>Kelime Değerlendir</title>
</head>

<body>
    <?php
    $image = $_POST['image'];
    $image = explode(',', $image);
    $image = $image[1];
    echo "Resmin ilk 20 karakteri: ".substr($image, 0, 20)."<br/>";

    $url = "";

    $json = json_encode(['image' => $image]);
    // echo "content json: ".$json."<hr/>";
    
    $options = ['http' => [
        'method' => 'POST',
        'header' => 'Content-type:application/json',
        'content' => $json
    ]];

    $context = stream_context_create($options);
    $response = file_get_contents($url, false, $context);

    echo "<h1>Response:".$response."</h1>";

    ?>
</body>

</html>
