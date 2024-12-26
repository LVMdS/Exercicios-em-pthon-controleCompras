import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import csv
import os

class ControleMensalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Controle Mensal")
        self.root.geometry("600x500")
        
        self.despesas = []
        self.csv_file_path = ""

        # Labels e Entradas para informações
        tk.Label(root, text="Caminho do arquivo CSV:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_csv_path = tk.Entry(root, width=50)
        self.entry_csv_path.grid(row=0, column=1, padx=5, pady=5)

        self.btn_browse = tk.Button(root, text="Procurar", command=self.selecionar_arquivo)
        self.btn_browse.grid(row=0, column=2, padx=5, pady=5)

        tk.Label(root, text="Local da Compra:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_local = tk.Entry(root)
        self.entry_local.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(root, text="Data (dd/mm/yyyy):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_data = tk.Entry(root)
        self.entry_data.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(root, text="Valor (R$):").grid(row=3, column=0, padx=5, pady=5)
        self.entry_valor = tk.Entry(root)
        self.entry_valor.grid(row=3, column=1, padx=5, pady=5)
        
        # Botão para adicionar despesa
        self.btn_add = tk.Button(root, text="Adicionar Despesa", command=self.adicionar_despesa)
        self.btn_add.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Tabela para exibir as despesas
        self.tabela = ttk.Treeview(root, columns=("Local", "Data", "Valor"), show="headings")
        self.tabela.heading("Local", text="Local")
        self.tabela.heading("Data", text="Data")
        self.tabela.heading("Valor", text="Valor (R$)")
        self.tabela.column("Local", width=150)
        self.tabela.column("Data", width=100)
        self.tabela.column("Valor", width=80)
        self.tabela.grid(row=5, column=0, columnspan=3, pady=10, padx=5, sticky="nsew")
        
        # Evento de duplo clique na tabela
        self.tabela.bind("<Double-1>", self.marcar_como_pago)
        
        # Campo para exibir o total das despesas não pagas
        self.label_total = tk.Label(root, text="Total de Despesas Não Pagas: R$ 0.00")
        self.label_total.grid(row=6, column=0, columnspan=3, pady=5)
        
        # Atualiza total se houver despesas já salvas
        self.carregar_despesas()

    def selecionar_arquivo(self):
        # Abre um diálogo para selecionar o arquivo CSV
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.entry_csv_path.delete(0, tk.END)
            self.entry_csv_path.insert(0, file_path)
            self.csv_file_path = file_path

    def carregar_despesas(self):
        # Carrega despesas do arquivo CSV se ele existir
        if os.path.exists(self.csv_file_path):
            with open(self.csv_file_path, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    despesa = {
                        "local": row["Local"],
                        "data": row["Data"],
                        "valor": float(row["Valor"]),
                        "pago": row["Pago"] == "True"
                    }
                    self.despesas.append(despesa)
                    if not despesa["pago"]:
                        self.tabela.insert("", "end", values=(despesa["local"], despesa["data"], f"R$ {despesa['valor']:.2f}"))

    def salvar_despesas(self):
        # Salva as despesas no arquivo CSV
        if self.csv_file_path:
            with open(self.csv_file_path, mode="w", newline="") as file:
                fieldnames = ["Local", "Data", "Valor", "Pago"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for despesa in self.despesas:
                    writer.writerow({
                        "Local": despesa["local"],
                        "Data": despesa["data"],
                        "Valor": despesa["valor"],
                        "Pago": despesa["pago"]
                    })

    def adicionar_despesa(self):
        try:
            # Obtém e valida os dados da entrada
            local = self.entry_local.get().strip()
            data_str = self.entry_data.get().strip()
            valor = float(self.entry_valor.get())
            
            # Validação da data
            data = datetime.strptime(data_str, "%d/%m/%Y")
            
            # Adiciona a despesa à lista e tabela
            despesa = {"local": local, "data": data_str, "valor": valor, "pago": False}
            self.despesas.append(despesa)
            self.tabela.insert("", "end", values=(local, data_str, f"R$ {valor:.2f}"))
            
            # Limpa as entradas
            self.entry_local.delete(0, tk.END)
            self.entry_data.delete(0, tk.END)
            self.entry_valor.delete(0, tk.END)
            
            # Atualiza o total das despesas não pagas
            self.atualizar_total()
            self.salvar_despesas()
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para o local, data e valor.")
    
    def marcar_como_pago(self, event):
        item_id = self.tabela.focus()
        if not item_id:
            return
        resposta = messagebox.askyesno("Marcar como Pago", "Esta despesa foi paga?")
        if resposta:
            # Atualiza o estado da despesa e remove da tabela
            valores = self.tabela.item(item_id, "values")
            for despesa in self.despesas:
                if despesa["local"] == valores[0] and despesa["data"] == valores[1] and f"R$ {despesa['valor']:.2f}" == valores[2]:
                    despesa["pago"] = True
                    self.tabela.delete(item_id)
                    break
            self.atualizar_total()
            self.salvar_despesas()
    
    def atualizar_total(self):
        total_nao_pago = sum(d["valor"] for d in self.despesas if not d["pago"])
        self.label_total.config(text=f"Total de Despesas Não Pagas: R$ {total_nao_pago:.2f}")

# Inicializa a interface
root = tk.Tk()
app = ControleMensalApp(root)
root.mainloop()
