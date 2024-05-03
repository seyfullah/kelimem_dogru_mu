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

    echo $response;
