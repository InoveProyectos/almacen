import { Box, Button, List, ListItem, ListItemText, TextField } from "@mui/material";
import React, { useState } from "react";

// Sin personalización de tema, utilizamos la paleta predeterminada de Material-UI
function AlmacenSaludable() {
  // Estado para los ingredientes y el menú sugerido
  const [ingredientes, setIngredientes] = useState([]);
  const [ingredienteInput, setIngredienteInput] = useState("");
  const [menuSugerido, setMenuSugerido] = useState([]);

  // Función para agregar un ingrediente
  const agregarIngrediente = () => {
    if (ingredienteInput && !ingredientes.includes(ingredienteInput)) {
      setIngredientes([...ingredientes, ingredienteInput]);
    }
    setIngredienteInput(""); // Limpiar el campo de entrada
  };

  // Función para sugerir menús saludables
  const sugerirMenu = () => {
    const menu = [];
    if (ingredientes.includes("Pollo") && ingredientes.includes("Arroz")) {
      menu.push("Arroz con Pollo");
    }
    if (ingredientes.includes("Tomate") && ingredientes.includes("Lechuga")) {
      menu.push("Ensalada Fresca");
    }
    if (ingredientes.includes("Pescado") && ingredientes.includes("Arroz")) {
      menu.push("Pescado a la Plancha con Arroz");
    }
    return menu.length > 0 ? menu : ["No hay suficiente para sugerir un menú"];
  };

  return (
    <Box sx={{ padding: 3 }}>
      <h2>Alimentos en tu Alacena</h2>

      {/* Campo de búsqueda de ingredientes */}
      <TextField
        label="Ingresa un ingrediente"
        variant="outlined"
        value={ingredienteInput}
        onChange={(e) => setIngredienteInput(e.target.value)}
        sx={{ marginBottom: 2 }}
      />
      <Button variant="contained" onClick={agregarIngrediente}>
        Agregar Ingrediente
      </Button>

      <h3>Ingredientes en tu alacena:</h3>
      <List>
        {ingredientes.map((ingrediente, index) => (
          <ListItem key={index}>
            <ListItemText primary={ingrediente} />
          </ListItem>
        ))}
      </List>

      {/* Botón para sugerir el menú */}
      <Button
        variant="contained"
        onClick={() => setMenuSugerido(sugerirMenu())}
        sx={{ marginTop: 2 }}
      >
        Sugerir Menú
      </Button>

      {/* Mostrar el menú sugerido */}
      {menuSugerido.length > 0 && (
        <Box sx={{ marginTop: 3 }}>
          <h3>Menú Sugerido:</h3>
          <List>
            {menuSugerido.map((menu, index) => (
              <ListItem key={index}>
                <ListItemText primary={menu} />
              </ListItem>
            ))}
          </List>
        </Box>
      )}
    </Box>
  );
}

export default AlmacenSaludable;
