/*
 * Zasady - https://pl.wikipedia.org/wiki/Papier,_kamie�,_no�yce
 * Autorzy - Karol Niemykin s16911 , Kacper Kaczor s16587
 * 
 * Przygotowanie �rodowiska:
 *  - Pobra� program Visual Studio Community ze strony -> https://visualstudio.microsoft.com/pl/vs/
 *  - Podczas instalacji zaznaczy� opcj� " Programowanie aplikacji klasycznych dla platformy .NET"
 *  - Pobra� projekt z Gita
 *  - Otworzy� Projekt w VS Studio 
 *  - Skompilowa� projekt
*/


using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace rockpaperscissors
{
    static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.SetHighDpiMode(HighDpiMode.SystemAware);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new GameWindow());
        }
    }
}
