import React, { useState } from 'react';
import { AppBar, Toolbar, IconButton, Typography, Drawer, List, ListItem, ListItemText, Divider, Button } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';

function App() {
  const [open, setOpen] = useState(false);

  const toggleDrawer = () => {
    setOpen(!open);
  };

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <AppBar position="sticky" style={{ backgroundColor: '#a8d5ba' }}> {/* Verde pastel */}
        <Toolbar>
          <IconButton edge="start" color="inherit" aria-label="menu" onClick={toggleDrawer}>
            <MenuIcon />
          </IconButton>
          
          {/* Logo */}
          <img src="/logo.png" alt="Logo" style={{ height: 60, marginRight: '10px' }} />
          
          <Typography variant="h6" style={{ color: '#f3e5ab' }}> {/* Color trigo */}
            Almacén Saludable
          </Typography>
        </Toolbar>
      </AppBar>

      {/* Menú Sandwich (Drawer) */}
      <Drawer anchor="left" open={open} onClose={toggleDrawer}>
        <List>
          <ListItem button>
            <ListItemText primary="Inicio" />
          </ListItem>
          <Divider />
          <ListItem button>
            <ListItemText primary="Productos" />
          </ListItem>
          <ListItem button>
            <ListItemText primary="Contacto" />
          </ListItem>
        </List>
      </Drawer>

      {/* Cuerpo principal (Body) */}
      <main style={{
        padding: '20px', 
        backgroundColor: '#fdfdfd',  // Blanco pastel
        flexGrow: 1, 
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',  // Centrado vertical
        alignItems: 'center',  // Centrado horizontal
        textAlign: 'center',  // Centrado del texto
        height: '100%', // Asegura que el main ocupe toda la altura restante
      }}>
        <h1 style={{ color: '#a8d5ba', fontSize: '7rem', marginBottom: '20px' }}>Bienvenido a Almacén Saludable</h1>
        <p style={{ color: '#333', fontSize: '2rem', marginBottom: '30px', maxWidth: '800px' }}>
          Compra productos frescos y saludables para tu hogar.
        </p>
        <Button variant="contained" color="primary" style={{ backgroundColor: '#a8d5ba', fontSize: '1.5rem' }}>
          ¡Compra ahora!
        </Button>
      </main>

      {/* Footer */}
      <footer style={{
        padding: '20px', 
        textAlign: 'center', 
        backgroundColor: '#f1f1f1', 
        marginTop: 'auto'  // Esto asegura que el footer siempre esté al final
      }}>
        <Typography variant="body2" color="textSecondary">
          © 2024 Almacén Saludable. Todos los derechos reservados.
        </Typography>
      </footer>
    </div>
  );
}

export default App;
