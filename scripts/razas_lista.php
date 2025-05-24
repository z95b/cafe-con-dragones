<?php
echo "PHP funciona correctamente.";


header('Content-Type: application/json');

try {
    // Directorio donde están los archivos JSON
    $directory = 'razas/';

    // Verificar si el directorio existe
    if (!is_dir($directory)) {
        echo json_encode(["error" => "El directorio 'razas/' no existe. Verifica la ruta."]);
        exit;
    }

    // Escanear el directorio y filtrar solo los archivos JSON
    $files = array_filter(scandir($directory), function($file) use ($directory) {
        // Log de archivos encontrados (para depuración)
        if (is_file($directory . $file)) {
            error_log("Archivo encontrado: $file");
        }
        return is_file($directory . $file) && pathinfo($file, PATHINFO_EXTENSION) === 'json';
    });

    // Si no se encuentran archivos JSON
    if (empty($files)) {
        echo json_encode(["error" => "No se encontraron archivos JSON en el directorio 'razas/'."]);
        exit;
    }

    // Devolver los archivos JSON como un array
    echo json_encode(array_values($files));
} catch (Exception $e) {
    // Capturar cualquier error y devolverlo como JSON
    echo json_encode(["error" => "Error interno en el servidor: " . $e->getMessage()]);
    error_log("Error en lista_archivos.php: " . $e->getMessage());
    exit;
}
