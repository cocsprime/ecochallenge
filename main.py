import discord
from discord.ext import commands
import random

from config import TOKEN

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="$", intents=intents)

missoes = {}
pontos = {}

@bot.event
async def on_ready():
    print(f"Bot conectado com {bot.user}")
    await bot.tree.sync()
    bot.run(TOKEN)

# Função de missoes sustentaveis
@bot.tree.command(name="missao", description="Receba uma missao")
async def missao(interaction: discord.Interaction):
    uid = interaction.user.id

    if uid not in missoes:
        missoes[uid] = random.choice([
            "Reutilize um pote.",
            "Evite um copo descartavel.",
            "Separe o lixo reciclavel.",
            "Use os dois lados de uma folha."
        ])
    await interaction.response.send_message(f" Sua missão: {missoes[uid]}")

# Função para concluir a missão
@bot.tree.command(name="concluir", description="Conclua sua missão")
async def concluir(interaction: discord.Interaction):
    uid = interaction.user.id

    if uid not in missoes:
        await interaction.response.send_message("Você precisa usar /missao primeiro!")
        return
    del missoes[uid]
    pontos[uid] = pontos.get(uid, 0) + 10
    await interaction.response.send_message(f" Missão concluída! Você tem {pontos[uid]} pontos!")

bot.run(TOKEN)
