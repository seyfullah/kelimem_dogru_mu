<!DOCTYPE html>
<html lang="tr">

<head>
    <title>Kelime Uygulama</title>
</head>

<body>
    <h1>Kelimeler.csv İçeriği</h1>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = htmlspecialchars($_POST['fname']);
        if (empty($name)) {
            echo "Name is empty";
        } else {
            echo $name;
        }
    }
    $row = 1;
    if (($handle = fopen("Kelimeler.csv", "r")) !== false) {
        while (($data = fgetcsv($handle, 85, ",")) !== false) {
            $num = count($data);
            $row++;
            for ($c = 0; $c < $num; $c++) {
                echo $data[$c] . ", ";
            }
            echo "<br/>\n";
        }
        fclose($handle);
    }

    ?>
</body>

</html>