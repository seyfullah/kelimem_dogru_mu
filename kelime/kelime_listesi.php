<!DOCTYPE html>
<html lang="tr">

<head>
    <title>Kelime Uygulama</title>
</head>

<body>
    <h1>Kelimeler.csv İçeriği</h1>
    <?php
    $rowCount = 85;
    if (($handle = fopen("Kelimeler.csv", "r")) !== false) {
        while (($data = fgetcsv($handle, $rowCount, ",")) !== false) {
            $columnCount = count($data);
            for ($columnIndex = 0; $columnIndex < $columnCount; $columnIndex++) {
                echo $data[$columnIndex] . ", ";
            }
            echo "<br/>\n";
        }
        fclose($handle);
    }

    ?>
</body>

</html>