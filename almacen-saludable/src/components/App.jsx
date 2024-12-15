import { useMediaQuery, useTheme } from '@mui/material';

function App() {
  const [open, setOpen] = useState(false);
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

  const toggleDrawer = () => {
    setOpen(!open);
  };

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <AppBar position="sticky" style={{ backgroundColor: '#a8d5ba' }}>
        <Toolbar>
          <IconButton edge="start" color="inherit" aria-label="menu" onClick={toggleDrawer}>
            <MenuIcon />
          </IconButton>

          {/* Logo */}
          <img src="/logo.png" alt="Logo" style={{ height: 60, marginRight: '10px' }} aria-label="Logo Almacén Saludable" />

          <Typography variant="h6" style={{ color: '#fdfdfd' }}>
            Almacén Saludable
          </Typography>
        </Toolbar>
      </AppBar>

      {/* Menú Sandwich (Drawer) */}
      <Drawer anchor="left" open={open} onClose={toggleDrawer} variant={isMobile ? 'temporary' : 'persistent'}>
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
        backgroundColor: '#fdfdfd',
        flexGrow: 1,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        height: '100%',
      }}>
        <h1 style={{ color: '#a8d5ba', fontSize: '7rem', marginBottom: '20px' }}>Bienvenido a Almacén Saludable</h1>
        <p style={{ color: '#a8d5ba', fontSize: '2rem', marginBottom: '30px', maxWidth: '800px' }}>
          productos frescos y saludables para tu hogar.
        </p>
        <Button variant="contained" color="primary" style={{ backgroundColor: '#a8d5ba', fontSize: '1.5rem', color: '#fdfdfd' }}>
          ¡ELIGE EL TUYO!
        </Button>
      </main>

      {/* Aquí se renderiza el componente */}
      <AlmacenSaludable />

      {/* Footer */}
      <footer style={{
        padding: '20px',
        textAlign: 'center',
        backgroundColor: '#f1f1f1',
        marginTop: 'auto'
      }}>
        <Typography variant="body2" color="textSecondary">
          © 2024 Almacén Saludable. Todos los derechos reservados.
        </Typography>
      </footer>
    </div>
  );
}

export default App;
